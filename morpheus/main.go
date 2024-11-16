package main

import (
	"crypto/tls"
	"crypto/x509"
	"errors"
	"fmt"
	"log"
	. "morpheus/src"
	. "morpheus/src/protogen"
	"morpheus/src/sec"
	"net"
	"os"
	"strings"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
)

const (
    NO_MTLS_ENV = "MORPHEUS_DISABLE_MTLS"
    PORT_ENV = "MORPHEUS_PORT"
    CA_CERT_PATH_ENV = "MORPHEUS_CA_PEM"
    SERVER_CERTS_PATHS_ENV = "MORPHEUS_SERVER_MTLS_CERTS"
    JWT_AUTH_PUBLIC_KEY_ENV = "MORPHEUS_JWT_SECRET_PATH"

    GREETING_HEADER=`
  __  __                  _                    
 |  \/  |                | |                   
 | \  / | ___  _ __ _ __ | |__   ___ _   _ ___ 
 | |\/| |/ _ \| '__| '_ \| '_ \ / _ \ | | / __|
 | |  | | (_) | |  | |_) | | | |  __/ |_| \__ \
 |_|  |_|\___/|_|  | .__/|_| |_|\___|\__,_|___/
                   | |                         
                   |_|
`
)

func getEnvOrDefault(key, defaultValue string) string {
    trueSupplier := func(str string) bool {
        return true
    }

    value, _ := getValidEnvOrDefault(key, defaultValue, trueSupplier)
    return value
}

func getValidEnvOrDefault(key, defaultValue string, isValid func(string) bool) (string, error) {
    value := os.Getenv(key)
    if len(value) == 0 {
        if !isValid(defaultValue) {
            return "", fmt.Errorf("Env not set for var: '%v' and fallback value '%s' is not valid", key, defaultValue)
        }
        return defaultValue, nil
    }
    if !isValid(value) {
        return "", fmt.Errorf("Env value for key '%v' is set to '%v' and is invalid", key, value)
    }
    return value, nil
}

func loadMtlsCaPool() (*x509.CertPool, error) {
    mtlsCaPool := x509.NewCertPool()
    caCertFilepath := getEnvOrDefault(CA_CERT_PATH_ENV, "./ca.crt.pem")
    certificate, err := os.ReadFile(caCertFilepath)
	if err != nil {
        return nil, err
	}

    ok := mtlsCaPool.AppendCertsFromPEM(certificate)
    if !ok {
		return nil, errors.New("Failed to append client certs")
	}

    log.Printf("CA cert file path successfully loaded from: '%v'", caCertFilepath)
    return mtlsCaPool, nil
}

func loadServerCertificates() ([]tls.Certificate, error) {
    paths := strings.Fields(getEnvOrDefault(SERVER_CERTS_PATHS_ENV, "./server"))
    certs := make([]tls.Certificate, len(paths))
    for i, path := range paths {
        currCert, err := tls.LoadX509KeyPair(path + ".crt", path + ".key")
        if err != nil {
            return nil, err
        }
        certs[i] = currCert
    }

    return certs, nil
}

func loadTlsConfig() (*tls.Config, error) {
    caPool, err := loadMtlsCaPool()
    if err != nil {
        return nil, err
    }

    serverCertificates, err := loadServerCertificates()
    if err != nil {
        return nil, err
    }
    
    return &tls.Config{
        ClientAuth: tls.RequireAndVerifyClientCert,
        Certificates: serverCertificates,
        ClientCAs: caPool,
    }, nil
}

func loadJwtAuthenticator() (*sec.JwtAuthenticator, error) {
    publicKey, err := os.ReadFile(getEnvOrDefault(JWT_AUTH_PUBLIC_KEY_ENV, ""))
    if err != nil {
        return nil, err
    }

    return sec.NewJwtAuthenticator(publicKey)
}

func NewGrpcServer() (*grpc.Server, error) {
    if strings.TrimSpace(getEnvOrDefault(NO_MTLS_ENV, "0")) == "1" {
        return grpc.NewServer(), nil
    }

    tlsConfig, err := loadTlsConfig()
    if err != nil {
        return nil, err
    }
    creds := grpc.Creds(credentials.NewTLS(tlsConfig))
	return grpc.NewServer(creds), nil
}

func main() {
    fmt.Printf(GREETING_HEADER);

    port := getEnvOrDefault(PORT_ENV, "8080")
	lis, err := net.Listen("tcp", ":" + port)
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

    jwtAuthenticator, err := loadJwtAuthenticator()
    if err != nil {
		log.Fatalf("Failed to create jwt authenticator: %v", err)
    }

    server, err := NewGrpcServer()
    if err != nil {
		log.Fatalf("Failed to create grpc server: %v", err)
    }
	RegisterMorpheusServer(server, NewMorpheusServer(jwtAuthenticator))

	log.Printf("Server is running on port %v...\n", port)
	if err := server.Serve(lis); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}

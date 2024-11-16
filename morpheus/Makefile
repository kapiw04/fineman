run-with-example-jwt-secret-no-mtls: setup build
	MORPHEUS_JWT_SECRET_PATH=./src/testdata/crypto/jwt_secret.pub.pem \
		MORPHEUS_DISABLE_MTLS=1 \
		./morpheus
run-with-example-secrets: setup build
	MORPHEUS_CA_PEM=./src/testdata/crypto/mtls/ca.crt \
		MORPHEUS_SERVER_MTLS_CERTS="./src/testdata/crypto/mtls/morpheus_a ./src/testdata/crypto/mtls/morpheus_b" \
		MORPHEUS_JWT_SECRET_PATH=./src/testdata/crypto/jwt_secret.pub.pem \
		./morpheus
protoc: setup
	 protoc  --go_out=. --go-grpc_out=. --proto_path=../proto morpheus.proto
setup:
	go mod tidy
build:
	go build
test:
	go test ./...


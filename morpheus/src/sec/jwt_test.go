package sec

import (
	"crypto/rand"
	"crypto/rsa"
	"log"
	"os"
	"testing"
	"time"

	"github.com/golang-jwt/jwt/v5"
	"github.com/stretchr/testify/assert"
)

const (
    SIGNED = iota
    SIGNED_NO_RSA = iota
    NOT_SIGNED = iota
    SIGNED_RSA_WRONG_KEY = iota
)

func TestJwtToUser(t *testing.T) {
    swt := signJwt(jwt.MapClaims{
        "exp": time.Now().Add(10 * time.Second).Unix(),
        "sub": "1",
    }, jwt.SigningMethodRS512, getPrivateSecret())
    user, err := createJwtAuthenticator().JwtToUser(swt)
    assert.Nil(t, err)
    assert.Equal(t, "1", user.GetUserId())
    assert.Empty(t, user.GetRoles())
    assert.Empty(t, user.GetPermissions())
}

func TestJwtToUserExpiredJwt(t *testing.T) {
    swt := signJwt(jwt.MapClaims{
        "exp": time.Now().Add(-10 * time.Second).Unix(),
        "sub": "1",
    }, jwt.SigningMethodRS512, getPrivateSecret())
    _, err := createJwtAuthenticator().JwtToUser(swt)
    assert.ErrorContains(t, err, "expired")
}

func TestJwtToUserNoExpiryTime(t *testing.T) {
    swt := signJwt(jwt.MapClaims{
        "sub": "1",
    }, jwt.SigningMethodRS512, getPrivateSecret())
    _, err := createJwtAuthenticator().JwtToUser(swt)
    assert.ErrorContains(t, err, "no expiry time")
}

func TestJwtToUserWhenNoSubject(t *testing.T) {
    swt := signJwt(jwt.MapClaims{
        "exp": time.Now().Add(10 * time.Second).Unix(),
    }, jwt.SigningMethodRS512, getPrivateSecret())
    _, err := createJwtAuthenticator().JwtToUser(swt)
    assert.ErrorContains(t, err, "no subject")
}

func TestJwtToUserWrongSecret(t *testing.T) {
    key, err := rsa.GenerateKey(rand.Reader, 2048)
    assert.NoError(t, err)
    swt := signJwt(jwt.MapClaims{
        "exp": time.Now().Add(10 * time.Second).Unix(),
        "sub": "1",
    }, jwt.SigningMethodRS512, key)
    _, err = createJwtAuthenticator().JwtToUser(swt)
    assert.ErrorContains(t, err, "token signature is invalid")
}

func TestJwtToUserRolesIsString(t *testing.T) {
    swt := signJwt(jwt.MapClaims{
        "exp": time.Now().Add(10 * time.Second).Unix(),
        "sub": "1",
        "roles": "roles/viewer",
    }, jwt.SigningMethodRS512, getPrivateSecret())
    _, err := createJwtAuthenticator().JwtToUser(swt)
    assert.ErrorContains(t, err, "couldn't parse roles claims value as string[], couldn't resolve to an array")
}

func TestJwtToUserPermsIsStringsArray(t *testing.T) {
    swt := signJwt(jwt.MapClaims{
        "exp": time.Now().Add(10 * time.Second).Unix(),
        "sub": "1",
        "permissions": []string{"users.delete"},
    }, jwt.SigningMethodRS512, getPrivateSecret())
    user, err := createJwtAuthenticator().JwtToUser(swt)
    assert.NoError(t, err)
    assert.Equal(t, "1", user.GetUserId())
    assert.Empty(t, user.GetRoles())
    assert.Equal(t, []string{"users.delete"}, *user.GetPermissions())

}

func TestJwtToUserUnsigned(t *testing.T) {
    swt := signJwt(jwt.MapClaims{
        "exp": time.Now().Add(10 * time.Second).Unix(),
        "sub": "1",
    }, jwt.SigningMethodNone, getPrivateSecret())
    _, err := createJwtAuthenticator().JwtToUser(swt)
    assert.ErrorContains(t, err, "token contains an invalid number of segments")
}

func signJwt(claims jwt.Claims, signingMethod jwt.SigningMethod, secret interface{}) string {
    token := jwt.NewWithClaims(signingMethod, claims)
    if signingMethod == jwt.SigningMethodNone {
        res, err := token.SigningString()
        if err != nil {
            log.Fatalf("Couldn't get signing string, %v", err)
        }
        return res
    }
    swt, err := token.SignedString(secret)
    if err != nil {
        log.Fatalf("Couldn't sign JWT, %v", err)
    }

    return swt
}

func getPrivateSecret() *rsa.PrivateKey {
    privateToken, err := os.ReadFile("./../testdata/crypto/jwt_secret.pem")
    if err != nil {
        log.Fatalf("Can't read ./../testdata/crypto/jwt_secret.pem")
    }

    rsaPrivateKey, err := jwt.ParseRSAPrivateKeyFromPEM(privateToken)
    if err != nil {
        log.Fatalf("Can't parse ./../testdata/crypto/jwt_secret.pem to RSA private key")
    }

    return rsaPrivateKey
}

func createJwtAuthenticator() *JwtAuthenticator {
    token, err := os.ReadFile("./../testdata/crypto/jwt_secret.pub.pem")
    if err != nil {
        log.Fatalf("Can't read ./../testdata/crypto/jwt_secret.pub.pem")
    }

    authenticator, err := NewJwtAuthenticator(token)
    if err != nil {
        log.Fatalf("Can't create authenticator with RSA public key from ./../testdata/jwt_secret.pub.pem")
    }

    return authenticator
}

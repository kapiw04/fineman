package sec

import (
	"crypto/rsa"
	"errors"
	"fmt"
	"morpheus/src/dto"

	"github.com/golang-jwt/jwt/v5"
)


type JwtAuthenticator struct { 
    publicKey *rsa.PublicKey
}

func NewJwtAuthenticator(publicKey []byte) (*JwtAuthenticator, error) {
    key, err := jwt.ParseRSAPublicKeyFromPEM(publicKey)
    if err != nil {
        return nil, err
    }

    return &JwtAuthenticator{publicKey: key}, nil
}

func (authenticator *JwtAuthenticator) JwtToUser(token string) (*dto.User, error) {
    parsed, err := jwt.Parse(token, func(token *jwt.Token) (interface{}, error) {
        return authenticator.publicKey, nil
    })

    if err != nil {
        return nil, err
    }

    // parsed.Valid is responsible for the token being expired, wrongly signed
    // or signed by an untrusted party
    if claims, ok := parsed.Claims.(jwt.MapClaims); ok && parsed.Valid {
        if _, subjectExists := claims["sub"]; !subjectExists {
            return nil, errors.New("couldn't parse jwt, no subject")
        }
        if _, expExists := claims["exp"]; !expExists {
            return nil, errors.New("couldn't parse jwt, no expiry time")
        }
        return userFromClaims(claims)
    } else {
        return nil, errors.New("Invalid JWT Token")
    }
}

func userFromClaims(claims jwt.MapClaims) (*dto.User, error) {
    userId, err := claims.GetSubject()
    if err != nil {
        return nil, err
    }

    rolesArr, permissionsArr := &[]string{}, &[]string{}
    if roles, exists := claims["roles"]; exists {
        rolesArr, err = toStringsArray(roles)
        if err != nil {
            return nil, fmt.Errorf("couldn't parse roles claims value as string[], %v", err)
        }
    }

    if permissions, exists := claims["permissions"]; exists {
        permissionsArr, err = toStringsArray(permissions)
        if err != nil {
            return nil, fmt.Errorf("couldn't parse permissions claims value as string[], %v", err)
        }
    }

    return dto.NewUser(userId, *rolesArr, *permissionsArr), nil
}

// Gets interface{} and returns pointer to a strings array 
// if given object can be represented as such, returns error otherwise
func toStringsArray(obj interface{}) (*[]string, error) {
    var elementsStringsSlice []string
    if elements, ok := obj.([]interface{}); ok {
        elementsStringsSlice = make([]string, len(elements))
        for i, element := range elements {
            if elementAsString, ok := element.(string); ok {
                elementsStringsSlice[i] = elementAsString
            } else {
                return nil, errors.New("couldn't resolve one of the elements as string")
            }
        }
    } else {
        return nil, errors.New("couldn't resolve to an array")
    }
    return &elementsStringsSlice, nil
}


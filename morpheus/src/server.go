package morpheus

import (
	"context"
	. "morpheus/src/protogen"
	"morpheus/src/sec"

	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

type MorpheusImpl struct {
    MorpheusServer
    jwtAuthenticator *sec.JwtAuthenticator
}

func NewMorpheusServer(jwtAuthenticator *sec.JwtAuthenticator) MorpheusServer {
    return &MorpheusImpl{jwtAuthenticator: jwtAuthenticator}
}

func (s *MorpheusImpl) PredictProductNames(ctx context.Context, request *PredictProductNamesRequest) (*PredictProductNamesResponse, error) {
    if _, jwtValidationError := s.jwtAuthenticator.JwtToUser(request.GetToken()); jwtValidationError != nil {
        return nil, status.Error(codes.PermissionDenied, "No JWT or invalid JWT")
    }

    return &PredictProductNamesResponse{PredictedProductNamesList: []*PredictedProductNames{}}, nil
}


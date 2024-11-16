// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v5.28.3
// source: morpheus.proto

package protogen

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.64.0 or later.
const _ = grpc.SupportPackageIsVersion9

const (
	Morpheus_PredictProductNames_FullMethodName = "/morpheus.Morpheus/PredictProductNames"
)

// MorpheusClient is the client API for Morpheus service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type MorpheusClient interface {
	PredictProductNames(ctx context.Context, in *PredictProductNamesRequest, opts ...grpc.CallOption) (*PredictProductNamesResponse, error)
}

type morpheusClient struct {
	cc grpc.ClientConnInterface
}

func NewMorpheusClient(cc grpc.ClientConnInterface) MorpheusClient {
	return &morpheusClient{cc}
}

func (c *morpheusClient) PredictProductNames(ctx context.Context, in *PredictProductNamesRequest, opts ...grpc.CallOption) (*PredictProductNamesResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(PredictProductNamesResponse)
	err := c.cc.Invoke(ctx, Morpheus_PredictProductNames_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// MorpheusServer is the server API for Morpheus service.
// All implementations must embed UnimplementedMorpheusServer
// for forward compatibility.
type MorpheusServer interface {
	PredictProductNames(context.Context, *PredictProductNamesRequest) (*PredictProductNamesResponse, error)
	mustEmbedUnimplementedMorpheusServer()
}

// UnimplementedMorpheusServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedMorpheusServer struct{}

func (UnimplementedMorpheusServer) PredictProductNames(context.Context, *PredictProductNamesRequest) (*PredictProductNamesResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method PredictProductNames not implemented")
}
func (UnimplementedMorpheusServer) mustEmbedUnimplementedMorpheusServer() {}
func (UnimplementedMorpheusServer) testEmbeddedByValue()                  {}

// UnsafeMorpheusServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to MorpheusServer will
// result in compilation errors.
type UnsafeMorpheusServer interface {
	mustEmbedUnimplementedMorpheusServer()
}

func RegisterMorpheusServer(s grpc.ServiceRegistrar, srv MorpheusServer) {
	// If the following call pancis, it indicates UnimplementedMorpheusServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&Morpheus_ServiceDesc, srv)
}

func _Morpheus_PredictProductNames_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PredictProductNamesRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MorpheusServer).PredictProductNames(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Morpheus_PredictProductNames_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MorpheusServer).PredictProductNames(ctx, req.(*PredictProductNamesRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Morpheus_ServiceDesc is the grpc.ServiceDesc for Morpheus service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Morpheus_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "morpheus.Morpheus",
	HandlerType: (*MorpheusServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "PredictProductNames",
			Handler:    _Morpheus_PredictProductNames_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "morpheus.proto",
}

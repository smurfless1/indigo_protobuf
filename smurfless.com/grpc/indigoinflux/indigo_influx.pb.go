// Code generated by protoc-gen-go. DO NOT EDIT.
// source: proto/indigo_influx.proto

package indigoinflux

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	timestamp "github.com/golang/protobuf/ptypes/timestamp"
	wrappers "github.com/golang/protobuf/ptypes/wrappers"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type InfluxTag struct {
	Name                 *wrappers.StringValue `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Folder               *wrappers.StringValue `protobuf:"bytes,2,opt,name=folder,proto3" json:"folder,omitempty"`
	XXX_NoUnkeyedLiteral struct{}              `json:"-"`
	XXX_unrecognized     []byte                `json:"-"`
	XXX_sizecache        int32                 `json:"-"`
}

func (m *InfluxTag) Reset()         { *m = InfluxTag{} }
func (m *InfluxTag) String() string { return proto.CompactTextString(m) }
func (*InfluxTag) ProtoMessage()    {}
func (*InfluxTag) Descriptor() ([]byte, []int) {
	return fileDescriptor_a8993388aedb6556, []int{0}
}

func (m *InfluxTag) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_InfluxTag.Unmarshal(m, b)
}
func (m *InfluxTag) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_InfluxTag.Marshal(b, m, deterministic)
}
func (m *InfluxTag) XXX_Merge(src proto.Message) {
	xxx_messageInfo_InfluxTag.Merge(m, src)
}
func (m *InfluxTag) XXX_Size() int {
	return xxx_messageInfo_InfluxTag.Size(m)
}
func (m *InfluxTag) XXX_DiscardUnknown() {
	xxx_messageInfo_InfluxTag.DiscardUnknown(m)
}

var xxx_messageInfo_InfluxTag proto.InternalMessageInfo

func (m *InfluxTag) GetName() *wrappers.StringValue {
	if m != nil {
		return m.Name
	}
	return nil
}

func (m *InfluxTag) GetFolder() *wrappers.StringValue {
	if m != nil {
		return m.Folder
	}
	return nil
}

type InfluxEvent struct {
	Measurement          *wrappers.StringValue `protobuf:"bytes,1,opt,name=measurement,proto3" json:"measurement,omitempty"`
	Time                 *timestamp.Timestamp  `protobuf:"bytes,2,opt,name=time,proto3" json:"time,omitempty"`
	Tags                 *InfluxTag            `protobuf:"bytes,3,opt,name=tags,proto3" json:"tags,omitempty"`
	Fields               *InfluxFields         `protobuf:"bytes,4,opt,name=fields,proto3" json:"fields,omitempty"`
	XXX_NoUnkeyedLiteral struct{}              `json:"-"`
	XXX_unrecognized     []byte                `json:"-"`
	XXX_sizecache        int32                 `json:"-"`
}

func (m *InfluxEvent) Reset()         { *m = InfluxEvent{} }
func (m *InfluxEvent) String() string { return proto.CompactTextString(m) }
func (*InfluxEvent) ProtoMessage()    {}
func (*InfluxEvent) Descriptor() ([]byte, []int) {
	return fileDescriptor_a8993388aedb6556, []int{1}
}

func (m *InfluxEvent) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_InfluxEvent.Unmarshal(m, b)
}
func (m *InfluxEvent) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_InfluxEvent.Marshal(b, m, deterministic)
}
func (m *InfluxEvent) XXX_Merge(src proto.Message) {
	xxx_messageInfo_InfluxEvent.Merge(m, src)
}
func (m *InfluxEvent) XXX_Size() int {
	return xxx_messageInfo_InfluxEvent.Size(m)
}
func (m *InfluxEvent) XXX_DiscardUnknown() {
	xxx_messageInfo_InfluxEvent.DiscardUnknown(m)
}

var xxx_messageInfo_InfluxEvent proto.InternalMessageInfo

func (m *InfluxEvent) GetMeasurement() *wrappers.StringValue {
	if m != nil {
		return m.Measurement
	}
	return nil
}

func (m *InfluxEvent) GetTime() *timestamp.Timestamp {
	if m != nil {
		return m.Time
	}
	return nil
}

func (m *InfluxEvent) GetTags() *InfluxTag {
	if m != nil {
		return m.Tags
	}
	return nil
}

func (m *InfluxEvent) GetFields() *InfluxFields {
	if m != nil {
		return m.Fields
	}
	return nil
}

type InfluxFields struct {
	On                   *wrappers.BoolValue  `protobuf:"bytes,1,opt,name=on,proto3" json:"on,omitempty"`
	Brightness           *wrappers.FloatValue `protobuf:"bytes,11,opt,name=brightness,proto3" json:"brightness,omitempty"`
	CoolSetpoint         *wrappers.FloatValue `protobuf:"bytes,20,opt,name=coolSetpoint,proto3" json:"coolSetpoint,omitempty"`
	HeatSetpoint         *wrappers.FloatValue `protobuf:"bytes,21,opt,name=heatSetpoint,proto3" json:"heatSetpoint,omitempty"`
	Temperature          *wrappers.FloatValue `protobuf:"bytes,22,opt,name=temperature,proto3" json:"temperature,omitempty"`
	Humidity             *wrappers.FloatValue `protobuf:"bytes,23,opt,name=humidity,proto3" json:"humidity,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
}

func (m *InfluxFields) Reset()         { *m = InfluxFields{} }
func (m *InfluxFields) String() string { return proto.CompactTextString(m) }
func (*InfluxFields) ProtoMessage()    {}
func (*InfluxFields) Descriptor() ([]byte, []int) {
	return fileDescriptor_a8993388aedb6556, []int{2}
}

func (m *InfluxFields) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_InfluxFields.Unmarshal(m, b)
}
func (m *InfluxFields) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_InfluxFields.Marshal(b, m, deterministic)
}
func (m *InfluxFields) XXX_Merge(src proto.Message) {
	xxx_messageInfo_InfluxFields.Merge(m, src)
}
func (m *InfluxFields) XXX_Size() int {
	return xxx_messageInfo_InfluxFields.Size(m)
}
func (m *InfluxFields) XXX_DiscardUnknown() {
	xxx_messageInfo_InfluxFields.DiscardUnknown(m)
}

var xxx_messageInfo_InfluxFields proto.InternalMessageInfo

func (m *InfluxFields) GetOn() *wrappers.BoolValue {
	if m != nil {
		return m.On
	}
	return nil
}

func (m *InfluxFields) GetBrightness() *wrappers.FloatValue {
	if m != nil {
		return m.Brightness
	}
	return nil
}

func (m *InfluxFields) GetCoolSetpoint() *wrappers.FloatValue {
	if m != nil {
		return m.CoolSetpoint
	}
	return nil
}

func (m *InfluxFields) GetHeatSetpoint() *wrappers.FloatValue {
	if m != nil {
		return m.HeatSetpoint
	}
	return nil
}

func (m *InfluxFields) GetTemperature() *wrappers.FloatValue {
	if m != nil {
		return m.Temperature
	}
	return nil
}

func (m *InfluxFields) GetHumidity() *wrappers.FloatValue {
	if m != nil {
		return m.Humidity
	}
	return nil
}

type SubscribeArgs struct {
	MulticastPort        uint32   `protobuf:"varint,1,opt,name=multicast_port,json=multicastPort,proto3" json:"multicast_port,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *SubscribeArgs) Reset()         { *m = SubscribeArgs{} }
func (m *SubscribeArgs) String() string { return proto.CompactTextString(m) }
func (*SubscribeArgs) ProtoMessage()    {}
func (*SubscribeArgs) Descriptor() ([]byte, []int) {
	return fileDescriptor_a8993388aedb6556, []int{3}
}

func (m *SubscribeArgs) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_SubscribeArgs.Unmarshal(m, b)
}
func (m *SubscribeArgs) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_SubscribeArgs.Marshal(b, m, deterministic)
}
func (m *SubscribeArgs) XXX_Merge(src proto.Message) {
	xxx_messageInfo_SubscribeArgs.Merge(m, src)
}
func (m *SubscribeArgs) XXX_Size() int {
	return xxx_messageInfo_SubscribeArgs.Size(m)
}
func (m *SubscribeArgs) XXX_DiscardUnknown() {
	xxx_messageInfo_SubscribeArgs.DiscardUnknown(m)
}

var xxx_messageInfo_SubscribeArgs proto.InternalMessageInfo

func (m *SubscribeArgs) GetMulticastPort() uint32 {
	if m != nil {
		return m.MulticastPort
	}
	return 0
}

func init() {
	proto.RegisterType((*InfluxTag)(nil), "indigo_influx.InfluxTag")
	proto.RegisterType((*InfluxEvent)(nil), "indigo_influx.InfluxEvent")
	proto.RegisterType((*InfluxFields)(nil), "indigo_influx.InfluxFields")
	proto.RegisterType((*SubscribeArgs)(nil), "indigo_influx.SubscribeArgs")
}

func init() {
	proto.RegisterFile("proto/indigo_influx.proto", fileDescriptor_a8993388aedb6556)
}

var fileDescriptor_a8993388aedb6556 = []byte{
	// 468 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x8c, 0x93, 0x5f, 0x6b, 0x13, 0x41,
	0x10, 0xc0, 0x4d, 0x0c, 0x41, 0x27, 0x8d, 0x96, 0xc5, 0x3f, 0x67, 0x2c, 0x56, 0x0e, 0x04, 0x11,
	0xb9, 0x94, 0x56, 0xf4, 0x41, 0x54, 0x0c, 0x58, 0xe9, 0x93, 0x72, 0x09, 0x3e, 0xf8, 0x52, 0xf6,
	0x2e, 0x73, 0x97, 0x85, 0xfd, 0x73, 0xec, 0xce, 0xf9, 0xe7, 0xdb, 0xfa, 0x15, 0xfc, 0x06, 0xa5,
	0xbb, 0xd7, 0xe3, 0x92, 0x16, 0x92, 0xc7, 0x9b, 0xfd, 0xfd, 0x66, 0x76, 0x66, 0xe7, 0xe0, 0x49,
	0x65, 0x0d, 0x99, 0xa9, 0xd0, 0x4b, 0x51, 0x9a, 0x73, 0xa1, 0x0b, 0x59, 0xff, 0x49, 0x7c, 0x8c,
	0x8d, 0xd7, 0x82, 0x93, 0xc3, 0xd2, 0x98, 0x52, 0xe2, 0xd4, 0x1f, 0x66, 0x75, 0x31, 0x25, 0xa1,
	0xd0, 0x11, 0x57, 0x55, 0xe0, 0x27, 0xcf, 0x36, 0x81, 0xdf, 0x96, 0x57, 0x15, 0x5a, 0x17, 0xce,
	0x63, 0x07, 0x77, 0xcf, 0x7c, 0xaa, 0x05, 0x2f, 0xd9, 0x11, 0x0c, 0x34, 0x57, 0x18, 0xf5, 0x9e,
	0xf7, 0x5e, 0x8e, 0x8e, 0x0f, 0x92, 0xe0, 0x26, 0x57, 0x6e, 0x32, 0x27, 0x2b, 0x74, 0xf9, 0x83,
	0xcb, 0x1a, 0x53, 0x4f, 0xb2, 0x37, 0x30, 0x2c, 0x8c, 0x5c, 0xa2, 0x8d, 0xfa, 0x3b, 0x38, 0x0d,
	0x1b, 0xff, 0xeb, 0xc1, 0x28, 0x54, 0xfd, 0xf2, 0x0b, 0x35, 0xb1, 0x8f, 0x30, 0x52, 0xc8, 0x5d,
	0x6d, 0x51, 0xa1, 0xa6, 0x9d, 0xca, 0x77, 0x05, 0x96, 0xc0, 0xe0, 0xb2, 0xef, 0xe6, 0x0e, 0x93,
	0x6b, 0xe2, 0xe2, 0x6a, 0x28, 0xa9, 0xe7, 0xd8, 0x6b, 0x18, 0x10, 0x2f, 0x5d, 0x74, 0xdb, 0xf3,
	0x51, 0xb2, 0x3e, 0xe8, 0x76, 0x1e, 0xa9, 0xa7, 0xd8, 0x09, 0x0c, 0x0b, 0x81, 0x72, 0xe9, 0xa2,
	0x81, 0xe7, 0x9f, 0xde, 0xc8, 0x9f, 0x7a, 0x24, 0x6d, 0xd0, 0xf8, 0x7f, 0x1f, 0xf6, 0xba, 0x07,
	0xec, 0x15, 0xf4, 0x8d, 0x6e, 0x5a, 0xbb, 0x7e, 0xc3, 0x99, 0x31, 0x32, 0x34, 0xd6, 0x37, 0x9a,
	0xbd, 0x07, 0xc8, 0xac, 0x28, 0x57, 0xa4, 0xd1, 0xb9, 0x68, 0xd4, 0x54, 0xdd, 0x74, 0x4e, 0xa5,
	0xe1, 0x14, 0xa4, 0x0e, 0xce, 0x3e, 0xc1, 0x5e, 0x6e, 0x8c, 0x9c, 0x23, 0x55, 0x46, 0x68, 0x8a,
	0x1e, 0x6c, 0xd7, 0xd7, 0x84, 0xcb, 0x04, 0x2b, 0xe4, 0xd4, 0x26, 0x78, 0xb8, 0x43, 0x82, 0xae,
	0xc0, 0x3e, 0xc0, 0x88, 0x50, 0x55, 0x68, 0x39, 0xd5, 0x16, 0xa3, 0x47, 0xdb, 0xfd, 0x2e, 0xcf,
	0xde, 0xc1, 0x9d, 0x55, 0xad, 0xc4, 0x52, 0xd0, 0xdf, 0xe8, 0xf1, 0x76, 0xb7, 0x85, 0xe3, 0xb7,
	0x30, 0x9e, 0xd7, 0x99, 0xcb, 0xad, 0xc8, 0xf0, 0xb3, 0x2d, 0x1d, 0x7b, 0x01, 0xf7, 0x54, 0x2d,
	0x49, 0xe4, 0xdc, 0xd1, 0x79, 0x65, 0x6c, 0x58, 0xad, 0x71, 0x3a, 0x6e, 0xa3, 0xdf, 0x8d, 0xa5,
	0xe3, 0x1c, 0xf6, 0x9b, 0x37, 0xb7, 0x5c, 0x3b, 0xc9, 0xc9, 0x58, 0xf6, 0x0d, 0xee, 0x87, 0x58,
	0x9b, 0x91, 0x1d, 0x6c, 0xbc, 0xfb, 0x5a, 0xad, 0xc9, 0xe4, 0xc6, 0xad, 0xf0, 0xfb, 0x1d, 0xdf,
	0x3a, 0xea, 0xcd, 0x16, 0x70, 0xe8, 0x54, 0x6d, 0x0b, 0x89, 0xce, 0x25, 0xb9, 0x51, 0xd3, 0xd2,
	0x56, 0x79, 0xf3, 0x8b, 0x07, 0x65, 0xb6, 0x7f, 0xe6, 0xbf, 0x82, 0xf9, 0xd5, 0x56, 0xf9, 0xcf,
	0x6d, 0x4a, 0x36, 0xf4, 0x13, 0x39, 0xb9, 0x08, 0x00, 0x00, 0xff, 0xff, 0xc2, 0xa8, 0x9c, 0xc8,
	0x32, 0x04, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// InfluxTranslatorClient is the client API for InfluxTranslator service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type InfluxTranslatorClient interface {
	InfluxSubscribe(ctx context.Context, in *SubscribeArgs, opts ...grpc.CallOption) (InfluxTranslator_InfluxSubscribeClient, error)
}

type influxTranslatorClient struct {
	cc grpc.ClientConnInterface
}

func NewInfluxTranslatorClient(cc grpc.ClientConnInterface) InfluxTranslatorClient {
	return &influxTranslatorClient{cc}
}

func (c *influxTranslatorClient) InfluxSubscribe(ctx context.Context, in *SubscribeArgs, opts ...grpc.CallOption) (InfluxTranslator_InfluxSubscribeClient, error) {
	stream, err := c.cc.NewStream(ctx, &_InfluxTranslator_serviceDesc.Streams[0], "/indigo_influx.InfluxTranslator/InfluxSubscribe", opts...)
	if err != nil {
		return nil, err
	}
	x := &influxTranslatorInfluxSubscribeClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type InfluxTranslator_InfluxSubscribeClient interface {
	Recv() (*InfluxEvent, error)
	grpc.ClientStream
}

type influxTranslatorInfluxSubscribeClient struct {
	grpc.ClientStream
}

func (x *influxTranslatorInfluxSubscribeClient) Recv() (*InfluxEvent, error) {
	m := new(InfluxEvent)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

// InfluxTranslatorServer is the server API for InfluxTranslator service.
type InfluxTranslatorServer interface {
	InfluxSubscribe(*SubscribeArgs, InfluxTranslator_InfluxSubscribeServer) error
}

// UnimplementedInfluxTranslatorServer can be embedded to have forward compatible implementations.
type UnimplementedInfluxTranslatorServer struct {
}

func (*UnimplementedInfluxTranslatorServer) InfluxSubscribe(req *SubscribeArgs, srv InfluxTranslator_InfluxSubscribeServer) error {
	return status.Errorf(codes.Unimplemented, "method InfluxSubscribe not implemented")
}

func RegisterInfluxTranslatorServer(s *grpc.Server, srv InfluxTranslatorServer) {
	s.RegisterService(&_InfluxTranslator_serviceDesc, srv)
}

func _InfluxTranslator_InfluxSubscribe_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(SubscribeArgs)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(InfluxTranslatorServer).InfluxSubscribe(m, &influxTranslatorInfluxSubscribeServer{stream})
}

type InfluxTranslator_InfluxSubscribeServer interface {
	Send(*InfluxEvent) error
	grpc.ServerStream
}

type influxTranslatorInfluxSubscribeServer struct {
	grpc.ServerStream
}

func (x *influxTranslatorInfluxSubscribeServer) Send(m *InfluxEvent) error {
	return x.ServerStream.SendMsg(m)
}

var _InfluxTranslator_serviceDesc = grpc.ServiceDesc{
	ServiceName: "indigo_influx.InfluxTranslator",
	HandlerType: (*InfluxTranslatorServer)(nil),
	Methods:     []grpc.MethodDesc{},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "InfluxSubscribe",
			Handler:       _InfluxTranslator_InfluxSubscribe_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "proto/indigo_influx.proto",
}

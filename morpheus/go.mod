module morpheus

require (
	github.com/golang-jwt/jwt/v5 v5.2.1
	github.com/stretchr/testify v1.9.0
	google.golang.org/grpc v1.68.0
	google.golang.org/protobuf v1.35.2
)

require (
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	golang.org/x/net v0.31.0 // indirect
	golang.org/x/sys v0.27.0 // indirect
	golang.org/x/text v0.20.0 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20241113202542-65e8d215514f // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)

// keep up to date with the github action go version
go 1.23.1

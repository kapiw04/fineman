# Morpheus
## gRpc service for guessing product names from OCRed receipts
--
Secured via mTls and identity propagation

Note that the service is just a mock and currently only returns empty responses.

### Proto excerpt:
```proto
message PredictProductNamesRequest {
    string receipt = 1;
    string token = 2;
}

message PredictedProductNames {
    repeated string predictedName = 1;
}

message PredictProductNamesResponse {
    repeated PredictedProductNames predictedProductNamesList = 1;
}

service Morpheus {
    rpc PredictProductNames (PredictProductNamesRequest) returns (PredictProductNamesResponse) {}
}
```

### Environment variables
* `MORPHEUS_DISABLE_MTLS` - if set to `1`, then server doesn't use mTls and disregards all other mTls related environment variables
* `MORPHEUS_PORT` - port on which the server will listen for requests
* `MORPHEUS_CA_PEM` - filepath where all concatenated CA certificates are stored in the `.pem` format
* `MORPHEUS_SERVER_MTLS_CERTS` - for each path `path`, server will try to interpret files `(path.crt, path.key)` as a pair of an mTls certificate and private key. Paths are passed in as a whitespace delimited list
* `MORPHEUS_JWT_SECRET_PATH` - path to public RSA key in the `.pem` format. Should be pointing to the same key, that is used for signing JWT during authentication

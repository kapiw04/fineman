# Morpheus
## Service for guessing product names from OCRed receipts

Note that the service currently only returns empty response.

Proto excerpt:
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

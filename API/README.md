### Morpheus gRpc client generation
Note: requires the `grpcio-tools` python3 package to be installed
```bash
# run in the /Api dir
python -m grpc_tools.protoc -I../proto --python_out=morpheus --pyi_out=morpheus --grpc_python_out=morpheus ../proto/morpheus.proto
```

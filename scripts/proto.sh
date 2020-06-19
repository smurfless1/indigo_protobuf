#!/bin/bash
set -eux

# =====
# automatically switch to the directory where the script lives
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pushd "${DIR}/.."
pwd
# =====

# =====
# set defaults
SOURCE=proto  # source of the proto files
TARGET=indigo_protobuf  # where to generate the python files
# =====

# =====
export GO111MODULE=on
which -s protoc-gen-go || go get github.com/golang/protobuf/protoc-gen-go@v1.3
export PATH="$PATH:$(go env GOPATH)/bin"
# =====

# =====
# work
TMPDIR=$(mktemp -d)
mkdir -p "${TMPDIR}/${TARGET}"
cp "${SOURCE}"/* "${TMPDIR}/${TARGET}"
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I "${TMPDIR}" "${TMPDIR}/${TARGET}/indigo.proto"
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I "${TMPDIR}" "${TMPDIR}/${TARGET}/indigo_influx.proto"
protoc -I . --python_betterproto_out=indigo_protobuf_betterproto proto/indigo.proto
protoc -I . --python_betterproto_out=indigo_protobuf_betterproto proto/indigo_influx.proto
protoc -I . proto/indigo.proto --go_out=plugins=grpc:.
protoc -I . proto/indigo_influx.proto --go_out=plugins=grpc:.


rm -rf "${TMPDIR}"
# =====

# =====
# return to the users calling dir
popd
# =====

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
# work
TMPDIR=$(mktemp -d)
mkdir -p "${TMPDIR}/${TARGET}"
cp "${SOURCE}"/* "${TMPDIR}/${TARGET}"
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I "${TMPDIR}" "${TMPDIR}/${TARGET}/indigo.proto"
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I "${TMPDIR}" "${TMPDIR}/${TARGET}/indigo_influx.proto"
protoc -I . --python_betterproto_out=indigo_protobuf_betterproto proto/indigo.proto
protoc -I . --python_betterproto_out=indigo_protobuf_betterproto proto/indigo_influx.proto

rm -rf "${TMPDIR}"
# =====

# =====
# return to the users calling dir
popd
# =====

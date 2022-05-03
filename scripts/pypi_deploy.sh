#!/bin/bash
set -eu

WORKDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="${WORKDIR}/.."
PYPI_REPO="prod"

main() {
    if ! git diff-files --quiet --ignore-submodules; then
        echo "The git workspace is not clean. Commit or stash your files before deploying."
        exit 1
    fi

    test_api_key=$(cat "$TEST_PYPI_KEY_FILE")
    prod_api_key=$(cat "$PROD_PYPI_KEY_FILE")

    # create pypirc file
    sed "s/%%TEST_API_KEY%%/${test_api_key}/g; s/%%PROD_API_KEY%%/${prod_api_key}/g" "$PYPIRC_TEMPLATE" > "$PYPIRC_FILE"

    # deploy
    pushd "${REPO_ROOT}"

    rm -rf build dist

    python setup.py bdist_wheel

    twine upload \
        --disable-progress-bar \
        --repository "$PYPI_REPO" \
        --config-file "$PYPIRC_FILE" \
        --skip-existing \
        dist/*.whl
    popd
}

parse_args() {
    while (( "$#" )); do
        case "$1" in
            -d|--repo-root) REPO_ROOT=$2; shift 2 ;;
            -r|--pypi-repo) PYPI_REPO=$2; shift 2 ;;
            -h|--help) print_usage; exit 0 ;;
            -*) echo "Error: Unsupported flag $1" >&2; exit 1 ;;
            *) echo "Error: Unknown positional argument $1" >&2; exit 1 ;;
        esac
    done

    TMP_ROOT="${REPO_ROOT}/tmp"
    mkdir ${TMP_ROOT}
    PYPIRC_TEMPLATE="${REPO_ROOT}/scripts/pypirc.in"
    PYPIRC_FILE="${TMP_ROOT}/pypirc"

    TEST_PYPI_KEY_FILE="${TMP_ROOT}/test-pypi"
    PROD_PYPI_KEY_FILE="${TMP_ROOT}/prod-pypi"
}

print_usage() {
    cat << EOF
Deploy wheel(s) to PyPI.

Usage:
    ${0} <options>

Options:
    -d|--repo-root:  Specify the root of the repository (where setup.py lives). Defaults to script's parent directory.
    -r|--pypi-repo:  Specify the PyPI repository to use ('prod' or 'test'). Defaults to 'prod'.
    -h|--help:       Display this message.

EOF
}

parse_args "$@"
main

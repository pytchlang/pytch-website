#!/bin/bash

git status > /dev/null
if [ $? != 0 ]; then
    echo "Abandoning clean build"
    exit 1;
fi


REPO_ROOT=$(git rev-parse --show-toplevel)

cd "$REPO_ROOT" && (
    echo Working in $(pwd)

    echo
    echo Removing old build/html directory
    rm -r ./build/html

    echo
    echo Rebuilding HTML
    make html
)

#!/bin/bash

git status > /dev/null
if [ $? != 0 ]; then
    echo "Abandoning clean build"
    exit 1;
fi


REPO_ROOT=$(git rev-parse --show-toplevel)

cd "$REPO_ROOT" && (
    echo Working in $(pwd)

    setup_ok=yes
    for lnk in vm webapp; do
        if [ ! -e source/$lnk/index.rst ]; then
            echo "No index.rst found under source/$lnk; check sibling repos"
            setup_ok=no
        fi
    done

    if [ ! -e venv/bin/python ]; then
        echo "No Python virtualenv found in 'venv'"
        setup_ok=no
    fi

    if [ $setup_ok = no ]; then
        echo "Abandoning clean build"
        exit 1;
    fi

    . venv/bin/activate

    echo
    echo Removing old build directory
    rm -r ./build/html
    rm -r ./build/doctrees

    echo
    echo Rebuilding HTML
    make html
)

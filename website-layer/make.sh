#!/bin/bash

BUILD_DIR="$(realpath "$(dirname "$0")")"
REPO_ROOT="$(realpath "$BUILD_DIR"/..)"

cd "$REPO_ROOT"

LAYER_DIR=website-layer/layer-content

if [ -e venv -o -e $LAYER_DIR ]; then
    echo "Must be run in a clean clone"
    echo '(i.e., no "venv" or "'"$LAYER_DIR"'")'
    exit 1
fi


########################################################################
#
# Generate contents of build-info file.

BUILDINFOFILE=source/build-info.txt

if [ ! -e "$BUILDINFOFILE" ]; then
    echo Could not find source/build-info.txt in clone
    exit 1
fi

cat /dev/null > $BUILDINFOFILE

if [ ! -e ../.git ]; then
    echo 'Parent repo not found; must be run as git submodule'
    echo 'within pytch-releases'
    exit 1
fi

sha=$(git ls-remote .. HEAD | grep -v refs/remotes | cut -f 1)
printf "%-19s %s\n" pytch-releases $sha >> $BUILDINFOFILE

for sibling in \
        pytch-build \
        pytch-vm \
        pytch-webapp \
        pytch-website \
        pytch-tutorials \
; do
    sibling_repo=../$sibling
    if [ ! -e "$sibling_repo"/.git ]; then
        echo 'Sibling repo "'"$sibling"'" not found'
        exit 1
    fi
    sha=$(git ls-remote $sibling_repo HEAD | grep -v refs/remotes | cut -f 1)
    printf "%-19s %s\n" $sibling $sha >> $BUILDINFOFILE
done


########################################################################
#
# Create content and zip it


virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements_dev.txt

./bin/make-cleanly.sh

mkdir "$LAYER_DIR"
mv build/html "$LAYER_DIR"/doc

(
    cd "$LAYER_DIR"
    find doc -type d -print0 | xargs -0 chmod 755
    find doc -type f -print0 | xargs -0 chmod 644
    zip -r ../layer.zip doc
)


########################################################################
#
# Restore build-info file to avoid cluttering git status

git checkout -- $BUILDINFOFILE

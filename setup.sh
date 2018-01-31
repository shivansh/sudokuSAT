#!/bin/bash

set -eu

export Z3="$HOME/softwareDownloads/z3"
export LD_LIBRARY_PATH="$Z3/build"
export PYTHONPATH="$Z3/build/python"

localZ3="$(dirname $0)/z3"

# Check if the symlink is valid
if [ ! -e $localZ3 ] ; then
    ln -s "$Z3/build/python/z3" $localZ3
fi

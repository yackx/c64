#!/bin/zsh

set -e
for f in **/*.a; do
    if ! grep -q "* = " $f; then
        echo "Skipping $f"
        continue
    fi
    make TARGET=${f:r};
done

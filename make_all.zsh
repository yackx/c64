#!/bin/zsh

set -e
for f in **/*.a; do
    if ! grep -q -E "upstart\.a|\* =" $f; then
        echo "Skipping $f"
        continue
    fi
    make TARGET=${f:r};
done

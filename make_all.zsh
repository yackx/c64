#!/bin/zsh

set -e
for f in **/*.(a|asm); do
    if ! grep -q -E "upstart\.a|\* =" $f; then
        # No PC directory or no BASIC upstart found.
        # Must be a lib.
        echo "Skipping $f"
        continue
    fi
    make TARGET=${f:r};
    if [ $? -ne 0 ]; then
        echo "make failed for $f"
        exit 1
    fi    
done

#!/bin/zsh

set -e

for f in **/*.(a|asm); do
    echo "Format $f"
    python3 -m scripts.y_acme_fmt $f
done

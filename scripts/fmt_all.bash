#!/bin/bash

set -e

find . -type f \( -name "*.a" -o -name "*.asm" \) -print0 | while IFS= read -r -d '' f; do
    echo "Format $f"
    python3 -m scripts.y_acme_fmt "$f"
done
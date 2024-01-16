"""PC directive detection. Used by DCC6502 in Makefile."""

import re
import sys
from typing import IO, Optional


"""Detect the Program Counter (PC) directive.

The directeive is either:
- * = $xxxx
- *=$xxxx
- Inclusion of common/upstart.a

The PC will be returned as a string with 0x prefix, e.g. 0xc000.

@param f: The file to detect the PC directive in.
@return: The PC directive or None if no PC directive was found.
"""
def detect_start_pc_directive(f: IO) -> Optional[str]:
    content = f.read()

    # Look for upstart.a in the file content
    if 'common/upstart.a' in content:
        return '0x080d'

    # Find a line containing * = xxxx
    match = re.search(r'\*\s*=\s*\$([0-9A-Fa-f]+)', content)
    if match:
        return '0x' + match.group(1)

    return None


"""Print the start PC or exit."""
def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(('.a', '.asm')):
        print('Usage: python detect_start_pc.py <filename.a|filename.asm>')
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        start_pc = detect_start_pc_directive(f)

    if start_pc:
        print(start_pc)
    else:
        exit(1)


if __name__ == '__main__':
    main()
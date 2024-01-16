"""Skip bytes calculation. Used by DCC6502 in Makefile."""
import sys
from typing import Union


"""Compute the number of bytes to skip by DCC6502.

The number of bytes to skip is either 2 or 14,
based on the start PC:

- 14 bytes to skip if PC is 0x080d (BASIC upstart)
  = 2 bytes load address header + 12 bytes BASIC upstart itself.
- 2 is the default if start PC is not BASIC upstart,
  a.k.a there is a *= directive.

@param start_pc:
       The start PC. Either a string like '0xc000' or an integer (49152)
@return: The number of bytes to skip.
"""
def compute_skip_bytes(start_pc: str | int) -> int:
    if isinstance(start_pc, str) and start_pc.lower() == '0x080d':
        return 14
    else:
        return 2


"""Print the number of bytes to skip or exit."""
def main():
    if len(sys.argv) != 2:
        print('Usage: python compute_skip_bytes.py <start_pc>')
        sys.exit(1)

    skip_bytes = compute_skip_bytes(sys.argv[1])
    print(skip_bytes)


if __name__ == '__main__':
    main()

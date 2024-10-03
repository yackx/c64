"""Convert a text to a series of PETSCII or screen code files.

The text is typically a book or an article.
Each output file represents a page of the book.

- The asm version of the book reader (book-reader.acme) uses petscii files.
- The XC=BASIC version (book-reader.bas) uses screen codes.
"""

import sys
from typing import Literal

sys.path.append('../../')

import os
import textwrap

from scripts.ascii_converter import ascii_to_petscii_lower, ascii_to_screen_codes_lower

WIDTH = 40  # 40 for c64, preferably 80 for c128
BOOK_DIR = 'thoreau'
BOOK_FILE = 'disobedience.txt'
BOOK_INFO = 'info.bin'

# This script can convert the text to PETSCII or to screen codes.
# In case of screen codes, the output is right-padded to WIDTH.
MODE: Literal['petscii', 'screen_code']  = 'petscii'

# Prefix address, for screen codes. Optional.
# 0x0400 for instance is the default screen memory address for the C64.
# If the prefix address is set to 0x0400 for instance (C64 screen memory),
# the first byte of each output file will be $00, $04.
PREFIX_ADDRESS: [str | None] = 0x0400


def build():
    def convert(lines: [str]) -> [int]:
        if MODE == 'petscii':
            return convert_to_petscii(lines)
        elif MODE == 'screen_code':
            return convert_to_screen_codes(lines)
        else:
            raise ValueError(f'Unsupported mode: {MODE}')

    def convert_to_petscii(lines: [str]) -> [int]:
        single_str = ''.join(line + ('\r' if len(line) < WIDTH else '') for line in lines)
        return ascii_to_petscii_lower(single_str)

    def convert_to_screen_codes(lines: [str]) -> [int]:
        padded_lines = [line.ljust(WIDTH) for line in lines]
        single_str = ''.join(padded_lines)
        return ascii_to_screen_codes_lower(single_str)

    with open(os.path.join(BOOK_DIR, BOOK_FILE), 'r') as f_in:
        lines = f_in.readlines()

    wrapped_texts = [textwrap.wrap(line, width=WIDTH) for line in lines]
    wrapped_texts_with_blanks = [wl if wl != [] else [''] for wl in wrapped_texts]
    wrapped_lines = [item for sublist in wrapped_texts_with_blanks for item in sublist]
    current_line_number = 0
    current_page_number = 1

    while current_line_number < len(wrapped_lines):
        page = wrapped_lines[current_line_number:current_line_number+24]
        codes = convert(page)
        page_hex = f'{current_page_number:02x}'
        file_ext = 'scr' if MODE == 'screen_code' else 'pet'
        with open(os.path.join(BOOK_DIR, f'page{page_hex}.{file_ext}'), 'wb') as f_out:
            if PREFIX_ADDRESS is not None:
                f_out.write((PREFIX_ADDRESS & 0xff).to_bytes(1, 'big'))
                f_out.write((PREFIX_ADDRESS >> 8).to_bytes(1, 'big'))
            f_out.write(bytes(codes))

        current_line_number += 24
        current_page_number += 1        

    with open(os.path.join(BOOK_DIR, BOOK_INFO), 'wb') as f_out:
        f_out.write((current_page_number-1).to_bytes(1, 'big'))


if __name__ == "__main__":
    build()

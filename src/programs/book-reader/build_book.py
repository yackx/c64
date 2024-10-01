"""Convert a text book to a series of PETSCII files."""

import sys
sys.path.append('../../')

import os
import textwrap

from scripts.ascii_converter import ascii_to_petscii_lower

WIDTH = 40  # 40 for c64, preferably 80 for c128
BOOK_DIR = 'thoreau'
BOOK_FILE = 'disobedience.txt'
BOOK_INFO = 'info.bin'


def build():
    with open(os.path.join(BOOK_DIR, BOOK_FILE), 'r') as f_in:
        lines = f_in.readlines()

    wrapped_texts = [textwrap.wrap(line, width=WIDTH) for line in lines]
    wrapped_texts_with_blanks = [wl if wl != [] else [''] for wl in wrapped_texts]
    wrapped_lines = [item for sublist in wrapped_texts_with_blanks for item in sublist]
    current_line_number = 0
    current_page_number = 1

    while current_line_number < len(wrapped_lines):
        page = wrapped_lines[current_line_number:current_line_number+24]
        single_str = ''.join(line + ('\r' if len(line) < WIDTH else '') for line in page)
        petscii_codes: [int] = ascii_to_petscii_lower(single_str)
        hex = f'{current_page_number:02x}'
        with open(os.path.join(BOOK_DIR, f'page{hex}.pet'), 'wb') as f_out:
            f_out.write(bytes(petscii_codes))

        current_line_number += 24
        current_page_number += 1        

    with open(os.path.join(BOOK_DIR, BOOK_INFO), 'wb') as f_out:
        f_out.write((current_page_number-1).to_bytes(1, 'big'))


if __name__ == "__main__":
    build()

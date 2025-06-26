"""Convert a text to a series of PETSCII or screen code files.

The text is typically a book or an article.
Each output file represents a page of the book.

- The asm version of the book reader (book-reader.acme) uses petscii files.
- The XC=BASIC version (book-reader.bas) uses screen codes.
"""
import argparse
import os
import sys
import textwrap

sys.path.append('../../')

from scripts.ascii_converter import ascii_to_petscii_lower

# TODO Rename
BOOK_INFO = 'info.bin'
# TODO Rename
BOOK_INFO_2 = 'book_info.txt'
PAGE_COUNT_FILE = 'info.bin'


def convert(lines: [str], *, width: int) -> [int]:
    single_str = ''.join(line + ('\r' if len(line) < width else '') for line in lines)
    return ascii_to_petscii_lower(single_str)

def get_filename(*, output_mode, numbering, page_number) -> str:
    file_ext = 'scr' if output_mode == 'screen_code' else 'pet'
    file_base = f'page{page_number:02x}' if numbering == 'hex2' else f'page{page_number:03d}'
    return f'{file_base}.{file_ext}'


def build(*, book_dir: str, book_file: str, screen_width: int):
    with open(os.path.join(book_dir, book_file), 'r') as f_in:
        lines = f_in.readlines()

    wrapped_texts = [textwrap.wrap(line, width=screen_width) for line in lines]
    wrapped_texts_with_blanks = [wl if wl != [] else [''] for wl in wrapped_texts]
    wrapped_lines = [item for sublist in wrapped_texts_with_blanks for item in sublist]
    current_line_number = 0
    current_page_number = 1

    while current_line_number < len(wrapped_lines):
        page = wrapped_lines[current_line_number:current_line_number + 24]
        codes = convert(page, width=screen_width)
        file_name = f'page{current_page_number:02x}.pet'
        with open(os.path.join(book_dir, file_name), 'wb') as f_out:
            f_out.write(bytes(codes))

        current_line_number += 24
        current_page_number += 1

    # Write the number of pages to a file
    with open(os.path.join(book_dir, BOOK_INFO), 'wb') as f_out:
        f_out.write((current_page_number - 1).to_bytes(1, 'big'))


def parse_args():
    parser = argparse.ArgumentParser(
        description=
        "Convert a text to a series of PETSCII or screen code files. "
        "Currently, the ACME version of the book reader (book-reader.acme) uses PETSCII files, "
        "while the XC=BASIC version (book-reader.bas) uses screen codes. "
        "A load address must be specified for screen codes (typically screen memory address 0x0400)."
    )
    parser.add_argument('-d', '--book-dir', type=str, required=True, help='Book directory')
    parser.add_argument('-f', '--book-file', type=str, required=True, help='Book file name')

    # Screen width. Default is 40 for c64. Preferably 80 for c128.
    parser.add_argument('-w', '--width', type=int, default=40, help='Screen width')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    build(
        book_dir=args.book_dir,
        book_file=args.book_file,
        screen_width=args.width
    )

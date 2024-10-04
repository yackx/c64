"""Convert a long to a series of screen code files.

The text is typically a book or an article.
Each output file represents a page of the book and
is prefixed with a two-byte load address (e.g. 0x0400).
"""
import argparse
import os
import sys
import textwrap

sys.path.append('../../../../')

from scripts.ascii_converter import ascii_to_screen_codes_lower

LOAD_ADDRESS = 0x0400
BOOK_INFO_2 = 'info.txt'
PAGE_COUNT_FILE = 'page_count.txt'


def convert(lines: [str], width: int) -> [int]:
    padded_lines = [line.ljust(width) for line in lines]
    single_str = ''.join(padded_lines)
    return ascii_to_screen_codes_lower(single_str)


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
        file_name = f'page{current_page_number:03d}.scr'
        with open(os.path.join(book_dir, file_name), 'wb') as f_out:
            # Load address
            f_out.write((LOAD_ADDRESS & 0xff).to_bytes(1, 'big'))
            f_out.write((LOAD_ADDRESS >> 8).to_bytes(1, 'big'))
            # Page content
            f_out.write(bytes(codes))

        current_line_number += 24
        current_page_number += 1

    # Write the number of pages to a file
    with open(os.path.join(book_dir, PAGE_COUNT_FILE), 'w') as f_out:
        f_out.write(str(current_page_number - 1) + '\n')


def parse_args():
    parser = argparse.ArgumentParser(
        description=
        "Convert a text to a series of screen code files."
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

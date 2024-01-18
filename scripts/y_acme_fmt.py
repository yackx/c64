"""A basic formatter for ACME assembly code.

Does a decent job but does not cover all cases.

Usage: python y_acme_fmt.py <filename>
"""

from typing import IO
import io
import sys
import shutil
import os


def is_label(word: str) -> bool:
    if any(set(x) == set(word) for x in ['+', '-']):
        return True
    return word.endswith(':') or word.startswith('.')


def is_comment(fragment: str) -> bool:
    return fragment.lstrip().rstrip().startswith(';')

    
def _format_line(line: str) -> str:
    rstripped_line = line.rstrip()
    line = rstripped_line
    lstripped_line = rstripped_line.lstrip()
    
    if lstripped_line:
        first_char_position = len(rstripped_line) - len(lstripped_line)

        columns = [0, 12]

        if not lstripped_line.startswith(';'):
            # This is not a comment line
            current_or_next_column = next((col for col in columns if col >= first_char_position), None)
            if current_or_next_column is not None and first_char_position not in columns:
                # Move to the next column
                line = ' ' * current_or_next_column + lstripped_line
            elif current_or_next_column is None:
                # Beyond last column
                # Move to the last column
                line = ' ' * columns[-1] + lstripped_line

            words = line.split()
            if len(words) >= 2:
                if is_label(words[0]) and line.startswith(words[0]) and not is_comment(words[1]):
                    after_word_2 = line.removeprefix(words[0]).removeprefix(words[1]).lstrip()
                    line = words[0] + ' ' * (columns[1] - len(words[0])) + after_word_2


        comment_position = line.find(';')
        if comment_position != -1:
            # There is a comment
            comment = line[comment_position:]
            comment_columns = [0, 12, 44]
            current_or_next_comment_column = next((col for col in comment_columns if col >= comment_position), None)
            if current_or_next_comment_column is not None: # : and comment_position not in comment_columns:
                # Move the comment to the next column
                line = line[:comment_position] + ' ' * (current_or_next_comment_column - comment_position) + comment
            elif current_or_next_comment_column is None:
                # Comment beyond last column
                # Move the comment to the last column
                before_comment = line[:comment_position].rstrip()
                if len(before_comment) > comment_columns[-1]:
                    # Comment is beyond last column and there is no space before it
                    line = before_comment + ' ' + comment
                else:
                    line = before_comment + ' ' * (comment_columns[-1] - len(before_comment)) + comment   

    return line + '\n'


def format(file: IO[str]) -> IO[str]:
    output = io.StringIO()
    for line in file:
        output.write(_format_line(line))
    output.seek(0)
    return output


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python y_acme_fmt.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        original = file.read()
        file.seek(0)
        output = format(file)

    if output.getvalue() != original:
        backup_filename = filename + ".bak"
        shutil.copy(filename, backup_filename)
        with open(filename, 'w') as file:
            file.write(output.getvalue())
        os.remove(backup_filename)

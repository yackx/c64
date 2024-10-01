# A simple script to convert a ybas Commodore BASIC program to a vanilla BASIC program.
#
# See README.md for more information.

import os
import sys


def ybas_to_basic(input_path: str, output_path: str):
    ybas_program = read_input(input_path)
    basic_program = convert(ybas_program)
    write_output(basic=basic_program, path=output_path)


def read_input(path: str) -> [str]:
    if not path.endswith('.ybas'):
        raise ValueError('input file name must end in .ybas')
    with open(path, "r") as f:
        return f.readlines()


def write_output(*, basic: [str], path: str):
    with open(path, "w") as f:
        f.writelines([line + '\n' for line in basic])


def convert(ybas_program: [str]) -> [str]:
    program = []
    labels = {}
    basic_line_number = 10
    for i, line in enumerate(ybas_program):
        stripped = line.strip()
        if not stripped:
            continue  # Empty line
        if line == line.lstrip() and stripped.endswith(':'):
            # Label
            label = stripped[:-1]
            if label in labels.keys():
                raise ValueError(f'Duplicate label {label} found on line {i+1}')
            labels[label] = basic_line_number
        else:
            try:
                # Replace label by line number
                label = next(lab for lab in labels.keys() if lab in stripped)
                stripped = stripped.replace(label, str(labels[label]))
            except StopIteration:
                pass
            # Output + increment line number
            program.append(f'{basic_line_number} {stripped}')
            basic_line_number += 10
    return program


def usage():
    print(f'Usage: {sys.argv[0]} input_file\n')
    print('  input_file      A ybas Commodore BASIC program')
    print('\nybas will convert the input to a vanilla BASIC program.')
    print('Use petcat (a tool shipped with VICE) to create a .prg file afterwards.')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        exit(1)
    input_path = sys.argv[1]
    output_path = os.path.splitext(input_path)[0] + '.bas'
    try:
        ybas_to_basic(input_path, output_path)
        print(f'Converted to BASIC: {output_path}')
    except ValueError as e:
        print(f'Input error: {e}', file=sys.stderr)
        exit(1)
    except FileNotFoundError as e:
        print(f'File not found: {e}', file=sys.stderr)
        exit(1)


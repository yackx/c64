import sys
sys.path.append('../../../')

from scripts.ascii_converter import ascii_to_screen_codes


if __name__ == "__main__":
    with open('lorem.txt', 'r') as f_in:
        petscii_string = f_in.read()
    output_params = [
        (None, 'lorem_no_la.scr.bin'),  # No load address
        (0x0400, 'lorem_la.scr.bin'),  # Load address 0x0400
    ]
    for load_address, output_filename in output_params:
        screen_codes = ascii_to_screen_codes(petscii_string, load_address=load_address)
        with open(output_filename, 'wb') as f_out:
            f_out.write(bytes(screen_codes))

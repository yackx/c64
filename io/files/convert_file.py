import sys


def petscii_to_screen_codes(ascii_string, *, load_address=None):
    """Convert an ASCII string to C64 screen codes.
    
    See:
    https://sta.c64.org/cbm64pettoscr.html
    https://sta.c64.org/cbm64scrtopet.html
    
    @param ascii_string:
    The string to convert.

    @param load_address:
    If specified, the load address will be prepended to the output.

    @return:
    Screen codes as a list of integers.
    """
    screen_codes = []
    if load_address is not None:
        screen_codes.append(load_address & 0xff)
        screen_codes.append(load_address >> 8)
    for char in ascii_string:
        petscii_code = ord(char)
        print(f'{petscii_code:03d} {petscii_code} {char}')
        if 32 <= petscii_code <= 63 or 128 <= petscii_code <= 159:
            screen_code = petscii_code
        elif 64 <= petscii_code <= 95:
            screen_code = petscii_code - 64
        elif 96 <= petscii_code <= 127:
            screen_code = petscii_code + 64
        elif 160 <= petscii_code <= 191:
            screen_code = petscii_code - 64
        elif 192 <= petscii_code <= 223:
            screen_code = petscii_code + 32
        elif 224 <= petscii_code <= 255:
            screen_code = petscii_code - 32
        else:
            screen_code = petscii_code
        screen_codes.append(screen_code)
    return screen_codes


if __name__ == "__main__":
    with open('lorem.txt', 'r') as f_in:
        petscii_string = f_in.read()
    output_params = [
        (None, 'lorem_no_la.scr.bin'),  # No load address
        (0x0400, 'lorem_la.scr.bin'),  # Load address 0x0400
    ]
    for load_address, output_filename in output_params:
        screen_codes = petscii_to_screen_codes(petscii_string, load_address=load_address)
        with open(output_filename, 'wb') as f_out:
            f_out.write(bytes(screen_codes))

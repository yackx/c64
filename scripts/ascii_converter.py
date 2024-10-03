import sys


def ascii_to_petscii(ascii_string) -> [int]:
    """Convert an ASCII string to PETSCII.
    
    See:
    https://sta.c64.org/cbm64pettoscr.html
    https://sta.c64.org/cbm64scrtopet.html
    
    @param ascii_string:
    The string to convert.

    @return:
    PETSCII string.
    """
    petscii_codes = []
    for char in ascii_string:
        ascii_code = ord(char)
        # print(f'{ascii_code:03d} {ascii_code} {char}')
        if 97 <= ascii_code <= 122:
            petscii_code = ascii_code - 96
        elif 32 <= ascii_code <= 63 or 65 <= ascii_code <= 90:
            petscii_code = ascii_code
        elif 64 <= ascii_code <= 95:
            petscii_code = ascii_code + 32
        elif 96 <= ascii_code <= 127:
            petscii_code = ascii_code - 32
        elif 128 <= ascii_code <= 159:
            petscii_code = ascii_code
        petscii_codes.append(petscii_code)
    return petscii_codes


def ascii_to_petscii_lower(ascii_string) -> [int]:
    """Convert an ASCII string to PETSCII.
    
    @param ascii_string:
    The string to convert.

    @return:
    PETSCII string.
    """
    petscii_codes = []
    for char in ascii_string:
        ascii_code = ord(char)
        # print(f'{ascii_code:03d} {ascii_code} {char}')
        if 97 <= ascii_code <= 122:
            petscii_code = ascii_code - 32
        elif 65 <= ascii_code <= 90:
            petscii_code = ascii_code + 32
        elif 32 <= ascii_code <= 63:
            petscii_code = ascii_code
        elif ascii_code == 13:
            petscii_code = ascii_code
        petscii_codes.append(petscii_code)
    return petscii_codes


def ascii_to_screen_codes_lower(ascii_string, *, load_address=None):
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
        ascii_code = ord(char)
        # print(f'{ascii_code:03d} {ascii_code} {char}')
        if 97 <= ascii_code <= 122:
            screen_code = ascii_code - 96
        elif 32 <= ascii_code <= 63 or 65 <= ascii_code <= 90:
            screen_code = ascii_code
        elif ascii_code == 13:
            screen_code = 141
        elif 64 <= ascii_code <= 95:
            screen_code = ascii_code - 32
        else:
            raise ValueError(f'Invalid ASCII code: {ascii_code}')
        screen_codes.append(screen_code)
    return screen_codes


def ascii_to_screen_codes_upper(ascii_string, *, load_address=None):
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
        ascii_code = ord(char)
        # print(f'{ascii_code:03d} {ascii_code} {char}')
        if 32 <= ascii_code <= 63 or 128 <= ascii_code <= 159:
            screen_code = ascii_code
        elif 64 <= ascii_code <= 95:
            screen_code = ascii_code - 64
        elif 96 <= ascii_code <= 127:
            screen_code = ascii_code + 64
        elif 160 <= ascii_code <= 191:
            screen_code = ascii_code - 64
        elif 192 <= ascii_code <= 223:
            screen_code = ascii_code + 32
        elif 224 <= ascii_code <= 255:
            screen_code = ascii_code - 32
        else:
            screen_code = ascii_code
        screen_codes.append(screen_code)
    return screen_codes

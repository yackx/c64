import sys


def petscii_to_screen_codes(petscii_string):
    screen_codes = [chr(0), chr(4)]  # 2 bytes for the file location $0400
    for char in petscii_string:
        petscii_code = ord(char)
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
        screen_codes.append(chr(screen_code))
    return ''.join(screen_codes)


if __name__ == "__main__":    
    for line in sys.stdin:
        screen_codes = petscii_to_screen_codes(line)
        print(screen_codes, end='')  # end='' to avoid extra newline

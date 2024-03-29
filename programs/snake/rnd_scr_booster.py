"""
Generate screen addresses for food.

This scripts avoids the edges of the screen.

The generated byte sequence is to be copied
to the source code of the game.
"""
import random


if __name__ == '__main__':
    for i in range(int(32/4)):
        print('            !byte ', end='')
        for j in range(4):
            x = random.randint(0, 37) + 1
            y = random.randint(0, 22) + 1
            addr = 0x0400 + y * 40 + x
            h = "0x{:04x}".format(addr) 
            msb = h[2:4]
            lsb = h[4:6]
            print(f'${lsb}, ${msb}', end='')
            if j < 3:
                print(', ', end='')
        print()

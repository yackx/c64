# Memory layout

Mnemonic constants for memory layout (KERNAL, VIC-II, SID, CIA...)

Naming convention based on [Mapping the Commodore 64 - A comprehensive memory guide](https://doc.lagout.org/science/0_Computer%20Science/9_Others/Compute/Compute%27s_Mapping_the_Commodore_64.pdf) by Sheldon Leemon.

Example, at the beginning of a program:

```
            ;ACME 0.97
            !cpu 6510

            !src <lib/mmap/zp-free.acme>
            !src <lib/misc/upstart.acme>
```

For convenience, [mmap.acme](mmap.acme) is a meta library that includes all specific files. Instead of including many files individually, include [mmap.acme](mmap.acme).

```
            !src <lib/mmap/mmap.acme>
```

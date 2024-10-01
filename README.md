# Commodore 64 MOS 6502/6510 assembly routines

![C64 badge](/doc/logo.png)

**ASM routines and examples for the Commodore 64**

## Content 👀

In this repository:

- [src](/src) contains the source code of the routines and programs (see below)
- [doc](/doc)
  - [Addressing modes](/doc/addressing_modes.txt) summary
  - assemblers, editor code completion, IDE...
  - [Awesome references](/doc/references.md)
- [scripts](/scripts) - Python and bash utility scripts for this repository
- [ybas](/ybas) - A simple BASIC converter to use labels and avoid line numbers

The [src](/src) directory contains:

- [lib](/lib) - Reusable routines and macros written for ACME cross-assembler
- [lib-demo](/lib-demo) - Sample code (routines in action)
- [programs](/programs) - Illustrations of simple techniques
  - [Boring Snake](/programs/snake)
  - [c64 rules demo](/programs/c64-rules)
  - [Pacmunch](/programs/pacmunch)
  - one part in one day of [Advent of Code](/programs/aoc)
  - a simple [book reader]()
  - and some other random experiments

> [!TIP]
> Assume **PAL** for all VIC-II routines. Feel free to roam around the repository in no particular order but **read this page first**.

## Prerequisites 💪

You should be comfortable with the following topics:

- **Programming** and basic algorithms, in any language, preferably in the imperative category (C, Java, but also Python, JavaScript, etc). Prior exposure to C and Intel or ARM assembly language is a plus.
- **Base conversion** — decimal, binary, hexadecimal. This is the bread and butter of assembly programming.
- **Command line** — Understanding of `export`, `source`, `PATH` and `make`.

## References 📖

It is good to have these tabs opened in your browser:

- [c64.org](https://sta.c64.org/cbm64mem.html) - Memory map
- [c64os.com](http://www.c64os.com/post/6502instructions) - Neat presentation of instruction set
- [pagetable.com](https://www.pagetable.com/c64ref/6502/) - Instruction set, KERNAL API, ROM dissasembly, memory map, PETSCII chartset
- [oxyron.de](http://www.oxyron.de/html/opcodes02.html) - Simple table, illegal opcodes, bugs

At a minimum, keep the following reference handy:

- Memory map
- Instruction set
- Kernel tables

See also:

- [Awesome references](doc/references.md) 🕶️
- [Addressing modes cheatsheet](doc/addressing_modes.txt) 📩

## Toolchain ⛓️

To use the routines in this repository, the following tools are assumed:

- [ACME](https://github.com/meonwax/acme) - Cross-platform assembler.
- [VICE](https://vice-emu.sourceforge.io/) - Multi-platform emulator for C64 and other Commodore products.
- [c1541](https://vice-emu.sourceforge.io/) - Disk drive emulator.
- [petcat](https://vice-emu.sourceforge.io/) - ASCII/PETSCII converter.
- [dcc6502](https://github.com/tcarmelveilleux/dcc6502/blob/master/dcc6502.c) - Disassembler. Compile it yourself or use a package manager like `brew` on macOS.
- Any decent editor, preferably with syntax highlighting for ACME (vim, VSC, ...).
- `make` command.

ACME is the only one mandatory. There exists several of 6502/6510 cross assemblers, but our routines are written for ACME.

Any decent editor will suffice.

- `vim` and Visual Studio Code have plugins for ACME syntax highlighting.
- If you prefer an IDE, consider [CBM Studio](http://www.ajordison.co.uk/)
- or [WUDSN](https://www.wudsn.com/index.php/ide).

VICE ships with utilities that can be launched from the command line:

- `c1541` disk drive utility
- `petcat` ASCII/PETSCII converter (depending on the version)
- `x64sc` to launch the emulator itself

## (No) hardware ⌨️

Nothing beats the feeling of real hardware, but emulators are certainly convenient.

Deploying programs to an actual C64 (or anything close like a FPGA) is an option, but for simplicity, we will target and work with an emulator, a macro assembler from this era and a modern editor.

## Setup 🛠️

By default, the `Makefile` will look for tools and utilities in your `PATH`:

- `acme` - assembler
- `c1541` - disk drive emulator (ships with VICE)
- `x64sc` - VICE C64 emulator command
- `dcc6502` - disassembler

You can override the default values with environment variables. For instance on my macOS:

```bash
export ACME=`pwd`/c64/src
export C1541=/Applications/vice-gtk3-3.5/bin/c1541
export X64="open /Applications/vice-gtk3-3.5/x64sc.app"
export DCC6502=dcc6502
export PATH=`pwd`:$PATH
```

You **must** set `ACME` environment variable to the `src` folder of this project to allow the lib include directive to work.

> [!IMPORTANT]
> If you store `export` statements in a file, remember to `source` it, not to execute it.

## Extra 👍

- [Code completion](doc/completion.md)
- [IDE](doc/ide.md)

## Run 🏃‍♀️

Invoke `make` from the root of the repository to assemble, create a symbol table and a default disk image.

```bash
# Assemble and package `many.a`
make TARGET=src/programs/sprites/many
```

This will create:

- `many.prg` - Program file
- `many.a.sym` - Symbol table
- `many.d64` - Disk image
- `many.d` - Disassembled source code

Then run the program with:

```bash
# Launch emulator and auto-load
make TARGET=src/programs/sprites/many run
```

Programs in this repository are located at `$c000` by convention or use BASIC upstart for convenience.

- If the program contains a Program Counter (PC) directive, for instance `*=$c000`, type `SYS 49152` to run it from BASIC.
- If the program includes `common/upstart.a`, a [neat trick](common/upstart.a) will cause the asm program to run with `RUN`. Thanks to Vice `-autostart` option, the emulator will automatically load and run the program.

> **NOTE**
> The `Makefile` will automatically detect the PC directive and adjust the disassembler command accordingly.

The `Makefile` will also look for a local `Makefile` in the target directory. If found, it will be invoked. This allows for instance to add files to the generic disk image.

![C64 rules intro screen](/programs/c64-rules/c64-rules.gif)

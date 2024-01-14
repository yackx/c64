# Commodore 64 MOS 6502/6510 assembly routines

![C64 badge](/doc/logo.png)

**ASM routines and examples for the Commodore 64**

In this repository:

- Reusable routines and macros written in ACME cross-assembler
- Sample code (routines in action)
- [Programs](/programs) - Illustrations of basic techniques, [Boring Snake](/snake), [mini demo](/demo)
- [Documentation](/doc/) - Assemblers, editor code completion, IDE and [Awesome references](/doc/references.md).

Assume **PAL** for all VIC-II routines. Feel free to roam around the repository but **read this page first**.

## Prerequisites 💪

You should be comfortable with the following topics:

- **Programming** and basic algorithms, in any language, preferably in the imperative category (C, Java, but also Python, JavaScript, etc).
- **Base conversion** -- decimal, binary, hexadecimal. This is the bread and butter of assembly programming.
- **Command line** -- Understanding of `export`, `source`, `PATH` and `make` is required.

## References 📖

It is good to have these tabs opened in your browser:

- [c64.org](https://sta.c64.org/cbm64mem.html) - Memory map
- [c64os.com](http://www.c64os.com/post/6502instructions) - Neat presentation of instruction set
- [pagetable.com](https://www.pagetable.com/c64ref/6502/) - Instruction set, KERNAL API, ROM dissasembly, memory map, PETSCII chartset
- [oxyron.de](http://www.oxyron.de/html/opcodes02.html) - Simple table, illegal opcodes, bugs

At a minimum, keep the following reference handy:

- Memory map
- Instruction set

See also:

- [Awesome references](doc/references.md) 🕶️
- [Addressing modes cheatsheet](doc/addressing_modes.txt) 📩

## Toolchain ⛓️

You need to install the following tools:

- [ACME](https://github.com/meonwax/acme) - Cross-platform assembler.
- [VICE](https://vice-emu.sourceforge.io/) - Multi-platform emulator for C64 and other Commodore products.
- [dcc6502](https://github.com/tcarmelveilleux/dcc6502/blob/master/dcc6502.c) - Disassembler. Compile it yourself or use a package manager like `brew` on macOS.
- Any decent editor, preferably with syntax highlighting for ACME (vim, VSC, ...).
- `make` command.

ACME is the only one mandatory. There are tons of 6502/6510 cross assemblers, but our routines are written for ACME.

You can use any editor of your liking. `vim` and Visual Studio Code have plugins for ACME syntax highlighting. If you prefer an IDE, consider [CBM Studio](http://www.ajordison.co.uk/) or [WUDSN](https://www.wudsn.com/index.php/ide>).

VICE ships with utilities that can be launched from the command line:

- `c1541` disk drive utility
- `petcat` ASCII/PETSCII converter
- `x64sc` to launch the emulator itself

## (No) hardware ⌨️

Nothing beats the feel of real hardware, but emulators are certainly convenient.

Deploying programs to an actual C64 (or anything close like a FPGA) is an option, but for the sake of our mental sanity, we will target and work with an emulator, a macro assembler from this era and a modern editor.

## Setup 🛠️

By default, the `Makefile` will look for tools and utilities in your `PATH`:

- `acme` - assembler
- `c1541` - disk drive emulator (ships with VICE)
- `x64sc` - VICE C64 emulator command
- `dcc6502` - disassembler

You can override the default values with environment variables. For instance on my macOS:

```bash
export ACME=`pwd`/c64
export C1541=/Applications/vice-gtk3-3.5/bin/c1541
export X64="open /Applications/vice-gtk3-3.5/x64sc.app"
export DCC6502=dcc6502
export PATH=`pwd`:$PATH
```

You must set `ACME` env var to the root of the project to allow lib includes like `<common/addr.a>`.

> **NOTE**
> If you store `export` statements in a file, remember to `source` it, not to run it.

## Extra 👍

- [Code completion](doc/completion.md)
- [IDE](doc/ide.md)

## Run 🏃‍♀️

```bash
# Assemble and package from `many.a` in directory `sprites`
make TARGET=sprites/many
# Launch emulator and auto-load
make TARGET=sprites/many run
```

Programs in this repository are located at `$c000` by convention. Type `SYS 49152` to run them from BASIC. This is the default address for the `Makefile`. In several instances, depending on its layour, a program may be located at a different address. In that case, add a `START_PC` parameter to match the program's `*=` directive. For instance, if `*=$1000`:

```bash
make TARGET=charset/custom-font START_PC=0x1000 run
```

Demos may contain "BASIC upstart", e.g. they start with BASIC code containing a `SYS` call to execute the asm program. In that case, set `START_PC=0x080d D_SKIP_BYTES=14` to skip 14 bytes (12 bytes BASIC + the usual 2 bytes load address).

![C64 rules intro screen](/demo/c64-rules.gif)

# BASIC Upstart

Consider the following program the changes the screen background and border color rapidly:

```
            *= $0810 "Flicker"
            inc $d020
            inc $d021
            jmp start
```

You load it with

```
LOAD "FLICKER",8,1

SEARCHING FOR FLICKER
LOADING
READY
```

To run the program, you need to issue `SYS 2046`. It would be more convenient to simply `RUN`. We would need a BASIC upstart program to accomplish that task:

```
LIST
10 SYS 2046
```

That is what a **BASIC upstart** is for. Depending on the assembler, you have to provide the necessary routine (dasm) or use a built-in directive (KickAssembler).

- [dasm](upstart-dasm)
- [kick](upstart-kick)

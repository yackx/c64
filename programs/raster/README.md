# Raster interrupts

## Routines

- [Single IRQ](single-irq)
- [Double IRQ](double-irq)
- [Single IRQ loop](loop)

## Basic reading

Read [C64 Wiki](http://www.c64-wiki.com/index.php/Raster_interrupt)

## ACK IRQ

Acknowledging interrupts is achived by writing bit #0 of the _interrupt status register_ at `$d019`. Various techniques can be found using `DEC` or `ASL`.

From the [C= Forum](https://www.lemon64.com/forum/viewtopic.php?t=71355):

> The 6502 performs a memory access on every cycle. It takes a cycle to modify the value after it's been read, and they decided to make it write the original value back during that time and then write the new value.

> It's a documented quirk of the 6502 RMW addressing modes. They "fixed" it in the later 65**C**02 

## Bad lines

https://nurpax.github.io/posts/2018-06-19-bintris-on-c64-part-5.html

## Double IRQ

Very detailed, well explained.

https://codebase64.org/doku.php?id=base:double_irq_explained

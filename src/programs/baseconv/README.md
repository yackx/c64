# Decimal numbers

## BCD

[Introduction to Binary Coded Decimal](http://6502.org/tutorials/decimal_mode.html)

> BCD (Binary Coded Decimal) numbers can be directly added or subracted on the 6502 by using decimal mode. In BCD, a byte represents a number from 0 to 99, where $00 to $09 represents 0 to 9, $10 to $19 represents 10 to 19, and so on, all the way up to $90 to $99, which represents 90 to 99.

BCD calculations start with `SED` and typically end with `CLD`.

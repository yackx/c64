# ybas

**A simple BASIC converter to use labels and avoid line numbers.**

This is a very simple and limited script. If you are looking something more advanced, consider [XC=BASIC](https://xc-basic.net/).

## At a glance

The following program:

```
# cat sample.ybas

        print "hello"
loop:
        print "back"
        goto loop
```

will be turned into:

```
10 print "hello"
20 print "back"
30 goto 20
```

- No more line numbers.
- Use labels instead.

This converter is not a compiler. It has no idea about the BASIC syntax. It just replaces labels and adds line numbers.

The output can be turned into a PRG file using `petcat`:

```
$ petcat -w2 -o sample.prg sample.bas
```

## Usage

```
$ python ybas.py sample.ybas
```

X64 ?= x64
XC-BASIC ?= xcbasic3
C1541 ?= c1541

all: charset.d64

charset.prg: charset.bas
	$(XC-BASIC) $< $@

charset.d64: charset.prg
	$(C1541) -format "foobar,1" d64 `pwd`/$@ -write `pwd`/$< $(*F)

run: charset.d64
	$(X64) --args -autostart `pwd`/charset.d64

clean:
	rm charset.prg charset.d64 || true

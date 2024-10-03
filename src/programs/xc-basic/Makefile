X64 ?= x64
XC-BASIC ?= xcbasic3
C1541 ?= c1541

.PRECIOUS: %

MAKEFILE_DIR := $(shell realpath $(dir $(lastword $(MAKEFILE_LIST))))
BAS_FILES := $(wildcard *.bas)
PRG_FILES := $(BAS_FILES:.bas=.prg)
D64_IMAGES := $(BAS_FILES:.bas=.d64)

all: $(D64_IMAGES)

%.prg: %.bas
	$(XC-BASIC) $< $@

%.d64: %.prg
	$(C1541) -format "foobar,1" d64 `pwd`/$@ -write `pwd`/$< $(*F)

run: $(TARGET).d64
	$(X64) --args -autostart `pwd`/$(TARGET).d64

clean:
	rm -f $(PRG_FILES) $(D64_IMAGES)

# Generic Makefile for all programs in this repository.
# See instructions in README.md
# Example usage:
# make TARGET=src/program/hello run

C1541 ?= c1541
X128 ?= x128
ASM ?= acme
DCC6502 ?= dcc6502
PETCAT ?= petcat

.PRECIOUS: %

.PHONY: fmt

all: $(TARGET).d71 $(TARGET).d $(TARGET).prg

%.prg: %.acme
	$(ASM) -v1 -I `pwd` --color --strict-segments --cpu 8502 --format cbm --vicelabels $<.sym --outfile $@ $<

%.d71: %.prg
	$(C1541) -format "foobar,1" d71 `pwd`/$@ -write `pwd`/$< $(*F)
	# Execute local Makefile if it exists
	if [ -f `dirname $<`/Makefile ]; then make -C `dirname $<` C1541=$(C1541) BASENAME=`basename $(TARGET)`; fi

%.d: START_PC = $(shell python3 -m scripts.detect_start_pc $(TARGET).acme)
%.d: D_SKIP_BYTES = $(shell python3 -m scripts.compute_skip_bytes $(START_PC))
%.d: %.prg
	if [ -z "$(START_PC)" ]; then echo "START_PC: no PC directive found" && exit 1; else echo "START_PC set $(START_PC)"; fi
	echo "D_SKIP_BYTES set $(D_SKIP_BYTES)"
	$(DCC6502) -c -d -s $(D_SKIP_BYTES) -o $(START_PC) $< > $@

run: $(TARGET).d71
	$(X128) --args -autostart `pwd`/$(TARGET).d71 -moncommands `pwd`/$(TARGET).acme.sym

bas: $(TARGET).bas
	$(PETCAT) -w70 -o `pwd`/$(TARGET).prg `pwd`/$(TARGET).bas

run-bas: $(TARGET).prg	
	$(X128) --args -autostart `pwd`/$(TARGET).prg

fmt:
	$(shell python3 -m scripts.y_acme_fmt $(TARGET).a)

clean:
	find -E . -type f -regex '.*\.(sym|prg|d71|d)' -exec rm {} \;

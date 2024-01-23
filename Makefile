# See instructions in README.md

C1541 ?= c1541
X64 ?= x64sc
ASM ?= acme
DCC6502 ?= dcc6502
PETCAT ?= petcat

.PRECIOUS: %

.PHONY: fmt

all: $(TARGET).d64 $(TARGET).d $(TARGET).prg

%.prg: %.a
	$(ASM) -v1 -I `pwd` --color --strict-segments --cpu 6510 --format cbm --vicelabels $<.sym --outfile $@ $<

%.d64: %.prg
	$(C1541) -format "foobar,1" d64 `pwd`/$@ -write `pwd`/$< $(*F)
	# Execute local Makefile if it exists
	if [ -f `dirname $<`/Makefile ]; then make -C `dirname $<` C1541=$(C1541) BASENAME=`basename $(TARGET)`; fi

%.d: START_PC = $(shell python3 -m scripts.detect_start_pc $(TARGET).a)
%.d: D_SKIP_BYTES = $(shell python3 -m scripts.compute_skip_bytes $(START_PC))
%.d: %.prg
	if [ -z "$(START_PC)" ]; then echo "No PC directive found" && exit 1; fi
	$(DCC6502) -c -d -s $(D_SKIP_BYTES) -o $(START_PC) $< > $@

run: $(TARGET).d64
	$(X64) --args -autostart `pwd`/$(TARGET).d64 -moncommands `pwd`/$(TARGET).a.sym

bas: $(TARGET).bas
	$(PETCAT) -w2 -o `pwd`/$(TARGET).prg `pwd`/$(TARGET).bas

run-bas: $(TARGET).prg	
	$(X64) --args -autostart `pwd`/$(TARGET).prg

fmt:
	$(shell python3 -m scripts.y_acme_fmt $(TARGET).a)

clean:
	find -E . -type f -regex '.*\.(sym|prg|d64|d)' -exec rm {} \;

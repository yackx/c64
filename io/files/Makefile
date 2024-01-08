# See instructions in README.md

C1541 ?= c1541
X64 ?= x64sc
ASM ?= acme
DCC6502 ?= dcc6502
PETCAT ?= petcat
START_PC ?= 0xc000
D_SKIP_BYTES ?= 2

TARGET = d-load-file

.PRECIOUS: %

all: $(TARGET).d64 $(TARGET).d $(TARGET).prg

%.prg: %.a
	$(ASM) -v1 -I `pwd` --color --strict-segments --cpu 6510 --format cbm --vicelabels $<.sym --outfile $@ $<

%.d64: %.prg
	$(C1541) -format "foobar,1" d64 `pwd`/$@ -write `pwd`/$< $(*F)
	$(C1541) `pwd`/$@ -write `pwd`/lorem.scr.bin "lorem,u"

%.d: %.prg
	$(DCC6502) -c -d -s $(D_SKIP_BYTES) -o $(START_PC) $< > $@

run: $(TARGET).d64
	$(X64) --args -autostart `pwd`/$(TARGET).d64 -moncommands `pwd`/$(TARGET).a.sym

bas: $(TARGET).bas
	$(PETCAT) -w2 -o `pwd`/$(TARGET).prg `pwd`/$(TARGET).bas

run-bas: $(TARGET).prg	
	$(X64) --args -autostart `pwd`/$(TARGET).prg

clean:
	find -E . -type f -regex '.*\.(sym|prg|d64|d)' -exec rm {} \;

# See instructions in README.md
#
# Local Makefile that adds files to the disk image

C1541 ?= c1541

.PRECIOUS: %

default: d64

d64:
	$(C1541) `pwd`/$(BASENAME).d64 -write `pwd`/lorem_la.scr.bin "lorem la,u"
	$(C1541) `pwd`/$(BASENAME).d64 -write `pwd`/lorem_no_la.scr.bin "lorem no la,u"

clean:
	find -E . -type f -regex '.*\.(sym|prg|d64|d)' -exec rm {} \;

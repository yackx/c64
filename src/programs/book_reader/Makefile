# See instructions in README.md
#
# Local Makefile that adds files to the disk image

C1541 ?= c1541

BOOK_DIR = thoreau

.PRECIOUS: %

default: d64

d64:
	for i in {0..255}; do \
		hex=$$(printf "%02x" $$i); \
		if [ -f `pwd`/$(BOOK_DIR)/page$$hex.pet ]; then \
			$(C1541) `pwd`/$(BASENAME).d64 -write `pwd`/$(BOOK_DIR)/page$$hex.pet "page$$hex,u"; \
		fi \
	done; \
	$(C1541) `pwd`/$(BASENAME).d64 -write `pwd`/$(BOOK_DIR)/info.bin "info,u"; \

book:
	python build_book.py

clean:
	find -E . -type f -regex '.*\.(sym|prg|d64|d)' -exec rm {} \;

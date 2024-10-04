X64 ?= x64
XC-BASIC ?= xcbasic3
C1541 ?= c1541

BOOK_DIR = thoreau

all: book-reader.d64

book-reader.prg: book-reader.bas
	$(XC-BASIC) $< $@

book-reader.d64: book-reader.prg
	# Base program
	$(C1541) -format "foobar,1" d64 `pwd`/$@ -write `pwd`/$< $(*F)

	# Page count
	$(C1541) `pwd`/$@ -write `pwd`/$(BOOK_DIR)/page_count.txt "page-count,s"

	# Book info
	$(C1541) `pwd`/$@ -write `pwd`/$(BOOK_DIR)/info.txt "info,s"

	# Book files
	for i in {0..255}; do \
		dec3=$$(printf "%03d" $$i); \
		if [ -f `pwd`/$(BOOK_DIR)/page$$dec3.scr ]; then \
			$(C1541) `pwd`/$@ -write `pwd`/$(BOOK_DIR)/page$$dec3.scr "page$$dec3"; \
		fi \
	done; \

book:
	python build_book.py

run: book-reader.d64
	$(X64) --args -autostart `pwd`/book-reader.d64

clean:
	rm book-reader.prg book-reader.d64 || true

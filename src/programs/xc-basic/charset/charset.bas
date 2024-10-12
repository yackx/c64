REM Custom character set demo.
REM
REM Copy ROM charset to RAM then italicize.

REM Deactivate interrupts
POKE $DC0E, PEEK($DC0E) AND 254

REM Make character ROM visible at $d000-$dfff
POKE 1, PEEK(1) AND 251

REM Copy ROM to RAM
FOR r AS INT = $D000 TO $DFFF
    POKE r-40960, PEEK(r)
NEXT r

REM I/O area visible at $D000-$DFFF
POKE 1, PEEK(1) OR 4

REM Reactivate interrupts
POKE 56334, PEEK(56334) OR 1

REM Charset RAM at $3000 (sets soft character base address)
POKE $D018, PEEK($D018) AND 240 OR 12

REM Make characters italic by shifting each char
REM top 4 bytes 1 bit to the right (SHR)
PRINT "shift"
FOR r AS INT = $3000 TO $3FFF STEP 8
    FOR n AS INT = r TO r+4
        POKE n, SHR(PEEK(n), 1)
    NEXT n
NEXT r


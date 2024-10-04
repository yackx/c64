INCLUDE "colors.bas"

CONST DEVICE = 8
CONST SCREEN_RAM = $0400
CONST COLOR_RAM = $d800
CONST Y_MAX = 24
CONST X_MAX = 39

DECLARE SUB wait_any_key ()

DIM page_count AS BYTE

REM Color scheme
DIM char_color AS INT : REM PETSCII !
DIM bar_color AS INT
DIM err_color AS INT
DIM background_color AS INT
DIM border_color AS INT


REM Main menu screen
SUB screen_menu () STATIC
    PRINT "{CLR}{REV_ON}"
    PRINT "              BOOK READER              "
    PRINT "{REV_OFF}"
    PRINT "{DOWN}{DOWN}Use the following keys while reading:"
    PRINT ""
    PRINT "  F1. This page"
    PRINT "  F3. Previous page"
    PRINT "  F5. Next page"
    PRINT "   C. Color scheme"
    PRINT ""
    PRINT "Press any key to continue"
    CALL wait_any_key()
END SUB


REM Set color scheme
SUB set_color_scheme (scheme AS INT) STATIC
    SELECT CASE scheme
        CASE 2
            char_color = PETSCII_WHITE
            bar_color = COLOR_GRAY1
            err_color = COLOR_RED
            background_color = COLOR_BLACK
            border_color = COLOR_BLACK
        CASE 1
            char_color = PETSCII_BLACK
            bar_color = COLOR_GRAY1
            err_color = COLOR_RED
            background_color = COLOR_WHITE
            border_color = COLOR_WHITE
        CASE 3
            char_color = PETSCII_LBLUE
            bar_color = COLOR_GRAY3
            err_color = COLOR_WHITE
            background_color = COLOR_BLUE
            border_color = COLOR_LBLUE
    END SELECT

    BACKGROUND background_color
    BORDER border_color

    DIM r AS INT FAST
    bar_start = COLOR_RAM+40*(Y_MAX-1)
    FOR r = bar_start TO COLOR_RAM+40*(Y_MAX)
        POKE r, bar_color
    NEXT r

    REM Main color is applied using a
    REM PETSCII color sequence
    PRINT CHR$(char_color)
END SUB


REM Color scheme screen
SUB screen_color_scheme () STATIC
    PRINT "{CLR}"
    PRINT "Select a color scheme{DOWN}"
    PRINT "  1. Light theme"
    PRINT "  2. Dark theme"
    PRINT "  3. Commodore blue"

    DO
        DIM k$ AS STRING * 1
        DIM k AS BYTE
        GET k$
        k = VAL(k$)
    LOOP UNTIL k > 0 AND k <= 3

    CALL set_color_scheme(k)
END SUB


REM Display a message on the bottom bar
SUB bottom_bar (msg AS string * 39) STATIC
    TEXTAT 0, Y_MAX, msg, bar_color
    REM Delete till end of line
    FOR x AS BYTE = LEN(msg) TO X_MAX
        TEXTAT x, Y_MAX, " ", bar_color
    NEXT x 
END SUB


REM Clear the message bar
SUB clear_msg_bar () STATIC
    FOR x AS BYTE = 0 TO X_MAX
        TEXTAT x, Y_MAX, " "
    NEXT x 
END SUB


REM Load a page from disk to the screen
SUB load_page (page AS INT) STATIC
    ON ERROR GOTO load_error
    DIM page$ AS string * 16
    PRINT "{CLR}"

    REM File name
    page$ = STR$(page)
    DO UNTIL len(page$) = 3
        page$ = "0" + page$
    LOOP
    page$ = "page" + page$

    LOAD page$, DEVICE, SCREEN_RAM
    CALL bottom_bar(STR$(page) + "/" + STR$(page_count))
    
    EXIT SUB

load_error:
    CALL bottom_bar("Disk error: " + STR$(ERR()))
    EXIT SUB
END SUB


REM Load book information
SUB load_info () STATIC
    DIM title$ AS STRING * 40
    DIM author$ AS STRING * 40
    DIM year$ AS STRING * 4
    OPEN 2,8,2,"info,s,r"
    INPUT #2, title$, author$, year$
    TEXTAT 0,0,title$
    TEXTAT 0,2,author$
    TEXTAT 0,4,year$
    CLOSE 2
    CALL bottom_bar("press any key to continue")
END SUB


REM Load number of pages
SUB load_page_count () STATIC
    DIM count$ AS STRING * 4
    OPEN 2,8,2,"page-count,s,r"
    INPUT #2, count$
    CLOSE 2
    page_count = VAL(count$)
END SUB


SUB wait_any_key ()
    DO
        DIM k AS BYTE
        GET k
    LOOP UNTIL k > 0
END SUB


DIM page AS INT
page = 1
DIM done AS BYTE
done = 0
DIM load_it AS BYTE
load_it = 1

PRINT "{LOWER_CASE}"
PRINT "{CLR}"
CALL set_color_scheme(3)
CALL load_page_count()

main_loop:
DO
    ON ERROR GOTO err_handler
    IF load_it = 1 THEN
        CALL load_page(page)
    END IF
    load_it = 0

    DO
        DIM k AS BYTE
        GET k
    LOOP UNTIL k > 0

    SELECT CASE k
    CASE 133  ' {F1}
        CALL screen_menu()
        load_it = 1
    CASE 134  ' {F3}
        IF page > 1 THEN
            page = page - 1
            load_it = 1
        END IF
    CASE 135  ' {F5}
        page = page + 1
        load_it = 1
    CASE 81   ' "q"
        done = 1
    CASE 67   ' "c"
        CALL screen_color_scheme()
        load_it = 1
    END SELECT
LOOP UNTIL done = 1


err_handler:
CALL bottom_bar("Error: " + STR$(ERR()) + " [RETURN]")
CALL wait_any_key()
GOTO main_loop

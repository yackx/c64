/*---------------------------------------------------------------------------
Pac-munch - This crazy pacman will eat all characters on the screen.

@author Youri Ackx
---------------------------------------------------------------------------*/

.pc 		=	$0801				"Basic Upstart Program"
:BasicUpstart($0810)

.pc			=	$0810				"Pacman Muncher"

.const		RASTER_LINE = 251		// 251th line not visible on screen
.const		FRAME_SKIP = 1			// skip frames each tick
.const		SPRITE_CYCLE_SKIP = 4	// we move 4 pixels before animating sprite
.const		PACMAN_FRAMES = 4		// pacman is composed of 4 frames 
.const		PIXELS_PER_CHAR = 8		// encounter one char every 8 pixels
.const		MUNCHED_CHAR = $20		// white space
.const		END_ROW = 240

.const		CURRENT_CHAR = $12
.const		TMP_PTR = $10			// general purpose temporary ZP pointer

/*
@Y stores PIXELS_PER_CHAR counter
@X stores current SPRITE_CYCLE_SKIP
*/

/* Print an extra message to fill the screen */
print_msg:
			lda #<msg
			sta TMP_PTR
			lda #>msg
			sta TMP_PTR + 1			// store msg addr ptr
			ldy #$00				// character pointer
!loop:		lda (TMP_PTR), y		// load current char
			beq !done+				// 0 - reached end of string?
			jsr $ffd2				// chrout
			iny						// point to next char
			bne !loop-				// max 265 chars
!done:

/* Prepare sprite */
prepare_sprite:
			ldy #$00
!loop:		lda sprite, y			// move sprite bitmaps
			sta $2000, y			// to $2000
			iny
			bne !loop- 
			
  			lda #$80
    		sta $07f8				// sprite #0 at $2000
    		
			lda #$00
			sta $d010				// sprite #0 8th bit x left part

			lda #00
			sta $d000
			lda #66
			sta $d001				// sprite #0: x=0, y=66
			
			lda #$07
			sta $d027				// sprite #0 is yellow
			
			lda #$01
			sta $d015				// enable sprite #0
			
			lda #<$0400 + 3*40		// current char location
			sta CURRENT_CHAR		// is the first col of 3rd row
			lda #>$0400 + 3*40
			sta CURRENT_CHAR + 1	
			
			ldx #SPRITE_CYCLE_SKIP	// load sprite cycle skip counter
			ldy #00					// load pixels per char counter

/* Main loop */
main_loop:
			lda #RASTER_LINE
wait_rast:	cmp $d012				// busy wait for next raster line
			bne wait_rast

/* Munch character if applicable */
munch:
			lda $d010				// sprite #0: x > 255 ?
			beq on_char				// sprite #0 has x > 255
			lda $d000
			cmp #320-255-1			// sprite #0 x out of screen (right)?
			bcs x_test				// then don't try to munch char

on_char:	iny						// pacman is on a char
			cpy #PIXELS_PER_CHAR	// have we reached the next char?
			bne x_test				

munch_it:	lda #MUNCHED_CHAR		// pacman is on a new char
			ldy #00					// reset pixels per char counter
			sta (CURRENT_CHAR), y	// munch the char
			lda #PIXELS_PER_CHAR
			inc CURRENT_CHAR		// store new char location
			bne x_test
			inc CURRENT_CHAR + 1	// new char location high byte

/* Test on which part of the screen is sprite #0 */
x_test:		lda $d010				// sprite #0: x > 255 ?
			bne x_right				// sprite #0 has x > 255

/* Sprite #0 on the left part of the screen (x <= 255) */
x_left:		nop						// slow things down a little: less cycles
			nop						// take place on the left part of screen
			inc $d000				// move one pixel to the right
			bne cycle_sprite		// not reached yet end of left screen part
			inc $d010				// set sprite #0 8th bit x to right part
			jmp cycle_sprite

/* Sprite #0 on the right part of the screen (x > 255) */
x_right:	inc $d000				// move one pixel to the right
			lda $d000
			cmp #10+320-255+20		// reached right border?
			bne cycle_sprite
			lda #$00
			sta $d000
			sta $d010				// sprite #0: reset x to 0
			
			lda #7					
			adc $d001				// sprite #0: set y to next text line
			
			cmp #END_ROW
			bcs end					// done if reached bottom of screen
			sta $d001				// next text line: add 8 pixels to y

/* Animate the sprite #0 by cycling through the bitmap */
cycle_sprite:
			dex
			bne main_loop
			ldx #SPRITE_CYCLE_SKIP
			inc $07f8				// cycle through the sprite map
			lda $07f8				// in order to animate our pacman
			cmp #$80 + PACMAN_FRAMES - 1				
			bne main_loop
			lda #$80
			sta $07f8				// back to first bitmap bank
			bne main_loop

/* Done */
end:		rts

msg: 		.byte 13
			.fill 13, 32 .text "CRAZY PACMAN" .byte 13, 13
			.fill 11, 32 .text "IZ ON  UR SCREEN" .byte 13, 13
			.fill 12, 32 .text "EATING UR TEXT"
			.byte 0

sprite:
.import binary "pacman.bin"

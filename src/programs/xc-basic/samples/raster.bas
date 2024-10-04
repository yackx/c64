        option fastinterrupt
        background 0

        ' Set the 1st interrupt
        gosub irq_2

        system interrupt off
        raster interrupt on

        do
        loop while 1

irq_1:
        border 2
        on raster 120 gosub irq_2
        return

irq_2:
        border 1
        on raster 100 gosub irq_1
        return


    dim t as long
    on timer 10000 gosub irq_timer
    timer interrupt on
 
    print "press any key to quit"
    dim k as byte
    do
        get k
    loop until k > 0
    end

irq_timer:
    textat 0, 0, t
    t = t + 1
    return

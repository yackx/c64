open 2,8,2,"check,s,w"
print #2, 59
close 2

open 2,8,2,"check,s,r"
dim a$ as string * 4
input #2, a$
print a$
close 2

l = [0,False , 2, 0 , 1, 4, 5, 0 , 0 ,"a",0,0,0]

def move_zero(l):
    lc = len(l) - 1
    while lc >= 0:
        if l[lc] == 0 and type(l[lc]) is int:
            l.append(l.pop(lc))
        lc -=1
    return l

print(move_zero(l))


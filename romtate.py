st = "omid"
# not bad algoritm
def rotate(st, rotation):
    ls = list(st)
    r = rotation if rotation > 0 else rotation * -1
    for _ in range(0, r):
        if rotation < 0:
            ls.insert(0, ls.pop())
        else:
            ls.append(ls.pop(0))
    return "".join(ls)

# omidomid ..... pashmammmmmm
def rotate2(str, rotation):
    str_plus = st + st
    if rotation <= len(str):
        return str_plus[rotation:len(str)+rotation]
    else:
        return str_plus[rotation - len(str):rotation]



print(rotate2(st,5))

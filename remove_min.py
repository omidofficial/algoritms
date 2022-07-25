l = [10,6,4,3,4,3,9]

# bad coding
def remove_min(l):
    min = 0
    for i in l:
        if i < min:
            min = i
    
    return l.pop(l.index(min))

# print(remove_min(l))
# print(l)

# tamoome dade ha dr in algoritm kar mikond
def remove_miin(l):
    min = l[0]
    res = []
    for i in l:
        if i < min:
            min = i 
    for i in l:
        if i != min:
            res.append(i)
    return res


print(remove_miin(l))
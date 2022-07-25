l = [1, 7, 5, 3, 1, 100]
# l = [9,7,5,3,2,1]

def t(l):
    temp = 0
    result = []
    for i in range(len(l) - 1 ):
        r = l[i+1] - l[i]
        if temp < r:
            temp = r
        result.append(r) 
    
    return result.index(temp) + 1 if temp != 0 else temp

print(t(l))
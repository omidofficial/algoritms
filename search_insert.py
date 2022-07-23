lst = [1,2,3,4,5,7,8]
def search_insert(lst,num):
    temp = 0
    for i in lst :
        if i < num:
            temp = i
        elif i == num:
            return lst.index(i)
        elif i > num:
            if temp in lst:
                return lst.index(temp) + 1 
            return lst.index(i)
    return lst.index(temp) + 1

print(search_insert(lst,9))

def search(lst,val):
    low = 0
    high = len(lst) - 1 
    mid = len(lst) // 2 
    while low <= high :
        if val > lst[mid]:
            mid += 1
            low = mid 
        else:
            mid -= 1 
            high = mid 
    return low 

print(search(lst,5))


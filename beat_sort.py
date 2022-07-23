lst = [4,2,7,9,2,3,6]
# bad codeing
def beat_sort(lst):
    for j in range(0,len(lst)):
        temp = 0
        for i in range(1,len(lst)):
            if lst[temp] >= lst[i]:
                lst[i],lst[temp] = lst[temp],lst[i]
            temp = i
        
    return lst

print(beat_sort(lst))




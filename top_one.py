# lst = [1,1,2,2,3,4] ... [1,2] bishtarin tekrar

values = {
    "2":4,
    "4":2,
}
def top(arr):
    values = {}
    result = []
    max_num = 0
    for i in arr:
        if i in values:
            values[i] +=1
        else:
            values[i] = 1
    print(values)
    max_num = max(values.values())
    for k,v in values.items():
        if v == max_num :
            result.append(int(k))
    return result
    
print(top([1,1,1,2,2,2,4,3,2,1,5,5,5,5,3,2,1,4,5,7,8,9,6]))

    

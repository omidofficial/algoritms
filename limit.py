lst  = [1,2,3,4,5,6,7,8,9]

# me
def limit(ls,min=None,max=None):
    result = []
    for i in ls:
        if max == None:
            if i >= min:
                result.append(i)
        elif min == None:
            if i <= max:
                result.append(i)        
        elif i >= min and i <= max :
            result.append(i)
    
    return result


# best Algoritm 
def limit2(lst,min=None,max=None):
    check_min = lambda val: True if min is None else (min <= val)
    check_max = lambda val: True if max is None else (max >= val)

    return [val for val in lst if check_max(val) and check_min(val)]


# print(limit(lst,2,6))
print(limit2(lst))
# print(limit(lst,3,3))

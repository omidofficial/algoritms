l = [2, 5, 7, 11]
# bad time Complexity algoritm


def two_sum(lst, thesum):
    for i in range(0, len(lst)):
        for j in range(i, len(lst)):
            if lst[i] + lst[j] == thesum:
                return i, j


def two_sum2(lst, target):
    p1 = 0
    p2 = len(lst) - 1
    while p1 < p2:
        sum = lst[p1] + lst[p2]
        if sum == target:
            return p1, p2
        elif sum > target:
            p2 -= 1
        else:
            p1 += 1
        


# print(two_sum2(l, 18))


l = [1,4,6,7,9,10]

def twoo_sum(l,target):
    l1 = l[0]
    l2 = len(l) - 1 
    result = []
    while l1 < l2:
        res = l[l1] + l[l2]
        if target == res:
            result.append((l1,l2))
        elif target > res:
            l1 +=1
        else:
            l2 -=1
    return result if result else None

print(twoo_sum(l,16))


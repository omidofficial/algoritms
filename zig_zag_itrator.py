l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]
l3 = [11,12,13,14,15,16,17]
def zig(l1, l2):
    result = []
    for i in range(len(l1)):
        result.append(l1[i])
        result.append(l2[i])
    return result


print(zig(l1, l2))


def zig_multi(*args):
    all_lists = list(args)
    result = []
    while all_lists:
        l1 = all_lists.pop(0)
        result.append(l1.pop(0))
        if l1:
            all_lists.append(l1)
    return result


print(zig_multi(l1, l2))

from string import ascii_letters
lst = [1,2,4,3,5,6,7,8]

def limit(lst,min=None,max=None):
    max_check = lambda val: True if max is None else (val <= max)
    min_check = lambda val: True if min is None else (val >= min)

    return [num for num in lst if max_check(num) and min_check(num)]

# print(limit(lst,4))

lst2 = [1,2,2,1,4,6,1,2,3]

def top_one(lst):
    values = {}
    result = []
    for i in lst:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1 
    max_count = max(values.values())
    for key,val in values.items():
        if val == max_count:
            result.append(key)
    return result

# print(top_one(lst2))


"amir"
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encript(str,key=1,check_range=ascii_letters):
    result = ''
    for char in str:
        # if not char.isalpha():
        if False:
            result += char
        else:
            index = (check_range.index(char) + key) % len(check_range)
            result += check_range[index]
    return result

def decript(str,key,check_range=ascii_letters):
    key *= -1
    return encript(str,key,check_range)

# in algoritmi k man neveshtm use full nist va fght baraye yek range khasi 52, kar mikone.ag range taghir kone 
# baz bayad koli mohasebe konim
def brute_force(str):
    ehtemalat = {}
    for key in range(1,52):
        ehtemalat[key] = decript(str,key)
    return ehtemalat

# vli in code yek bar mohasebe shode va baraye hr range karbord dare 
def brute_force2(str,check_range=ascii_letters):
    ehtemalat = {}
    for key in range(1,len(check_range)):
        ehtemalat[key] = decript(str,key,check_range)
    return ehtemalat



c = ascii_letters + "123456789"
print(encript("1234",check_range=c))
print(brute_force2("2345",c))


# .......................................................





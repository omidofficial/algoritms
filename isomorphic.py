"fav" "kez"

# my rung way
def isomorphic(s1,s2):
    char_len = len(s1)
    maches = {}
    if char_len == len(s2):
        for i in range(0,char_len):
            if not (s1[i] and s2[i] in maches):
                maches[s1[i]] = s2[i]
                maches[s2[i]] = s1[i]

            else:
                if not maches[s1[i]] == s2[i] and maches[s2[i]] == s1[i]:
                    return False
                    break
        return True
                
# isomorphic("faa","lea")

# the True way 
def emo(s1,s2):
    if len(s1) != len(s2):
        return False
    dict = {}
    sett = set()
    for i in range(0,len(s1)):
        if s1[i] not in dict:
            if s2[i] in sett:
                return False
            dict[s1[i]] = s2[i]
            sett.add(s2[i])
        else:
            if dict[s1[i]] != s2[i]:
                return False
    return True

print(emo("faw","lee"))

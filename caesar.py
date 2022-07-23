# cipher  رمزنگاری
# caesar سزار
from string import ascii_letters
print(ascii_letters)

def encript(letter):
    result = ''
    for ch in letter:
        if not ch.isalpha():
            result += ch
        else:
            index = ascii_letters.index(ch) + 3
            the_index = index-52 if  index > 52 else index 
            result += ascii_letters[the_index]
    return result

def decript(letter):
    result = ""
    for ch in letter:
        if ch not in ascii_letters:
            result += ch
        else:
            index = ascii_letters.index(ch) - 3 
            result += ascii_letters[index]
    return result

print(encript("Zm@id"))
print(decript("cp@lg"))

# ........................................................


def sys_encript(letter,key):
    result = ''
    for ch in letter:
        if ch not in ascii_letters:
            result += ch
        else:
            index = (ascii_letters.index(ch) + key) % len(ascii_letters)
            result += ascii_letters[index]
    return result

def sys_decript(letter,key):
    key *= -1 
    return sys_encript(letter,key)

print(sys_encript("Zm@id",3))
print(sys_decript("cp@lg",3))
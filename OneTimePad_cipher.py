from random import randint
from traceback import print_tb


class OneTimePad:
    def encript(self,text):
        tex = [ord(i) for i in text]
        key = []
        cipher = []
        for i in tex:
            k = randint(1,300)
            c = k * i 
            key.append(k)
            cipher.append(c)
        return key,cipher

    def decript(self,key,cipher):
        dec = ""
        for i in range(0,len(cipher)):
            dec += (chr(cipher[i] // key[i]))
        return dec
vvv = OneTimePad()
k,c = vvv.encript("omid")
dec = vvv.decript(k,c)
print(dec)


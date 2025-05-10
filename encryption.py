f = open("not_crypted_text","r")
g = open("encrypted_text", "w")
key = input("key: ")
text = f.read()
key = key * (len(text)//len(key)+1)
key = list(key)
k = 0

for i in text:
    ct = 0
    a = i
    b = key[k]
    k += 1
    a = ord(a)
    b = ord(b)
    a=bin(a)
    b=bin(b)

    a = a[2:]
    b = b[2:]

    if(len(a)<8):
        a = (8-len(a))*"0" + a
    if(len(b)<8):
        b = (8-len(b))*"0" + b

    a = list(a)
    b = list(b)

    for i in a:
        a[ct] = int(a[ct])
        b[ct] = int(b[ct])
        a[ct] = a[ct]^b[ct]
        if a[ct] == 1:
            g.write("1")
        else:
            g.write("0")
        ct += 1
g.close()
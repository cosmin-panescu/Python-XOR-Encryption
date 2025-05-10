f = open( "encrypted_text", "r")
g = open( "decrypted_text", "w")
key = input("key: ")
text = f.read()
key = key* (len(text)//len(key)+1)
ct=0
cheie_binar = ""

for i in key:
    a = ord(i)
    a = bin(a)
    a = a[2:]
    if(len(a)<8):
        a = "0" * (8-len(a))+a
    cheie_binar = cheie_binar + a

sir_final = ""
cheie_binar = list(cheie_binar)
ct = 0
for i in text:
    a = int(i)
    b = int(cheie_binar[ct])
    ct += 1
    x = a^b
    if x == 0:
        sir_final = sir_final + "0"
    else:
        sir_final = sir_final + "1"

sir_final = sir_final[::-1]

suma = 0
ct = 0
sir_decriptat = ""
for i in sir_final:
    if ct == 8:
         ct = 0
         x = chr(suma)
         sir_decriptat = sir_decriptat + x
         suma = 0

    if i == "1":
        suma = suma + 2**ct
    ct += 1
x = chr(suma)
sir_decriptat = sir_decriptat + x

sir_decriptat = sir_decriptat[::-1]
g.write(sir_decriptat)
g.close()
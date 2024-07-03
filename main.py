def hitungsegitga(alas, tinggi):
    return(0.5*alas*tinggi)

def volume_balok(panjang, lebar, tinggi):
    hasil = panjang * lebar * tinggi
    return hasil

a = 3
b = 5

luas = hitungsegitga(a,b)

volume = volume_balok(4, 5, 10)
print("volume balok :", volume)

print("a =",a,"dan b",b,"dengan hasil",luas)

bebas = 'a'
baru = "bola"
sapi = bebas+baru
print(sapi)

baris = [1,2,3]
print(baris[1])

baris2 = [[2,4,3],
          [1,5,7],
          [0,9,5]]

print(baris2[1][2])

print(baru[2])

i = 0
iter = 1
penentu = 1
if (penentu==1):
    while (iter==1) :
        if (i==4):
            iter = 0

        print("hore",i+1,iter)
        i+=1
elif (penentu==0) :
    print("baiyoh")
else :
    print("ok")

baris3 = [[2,4,3],
          [1,5,7],
          [0,9,5]]
for i in range (3):
    for j in range (3):
        print (baris3[i][j])
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
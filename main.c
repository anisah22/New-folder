#include <stdio.h>

float hitungLuasSegitiga(int alas, int tinggi){
    float luas = 0.5 * alas * tinggi;
    return luas; 
}

int volume_balok (int panjang, int lebar, int tinggi){
    int hasil;
    hasil = panjang * lebar * tinggi;
    return hasil;
}

int main(){
    printf("halo\n");

    int a =3;
    int b = 5;

    int* pa = &a;

    printf("nilai integer adalah %d, berlokasi di pointer memori %p\n", a, pa);

    float luasan = hitungLuasSegitiga(a,b);
    printf("nilai luasan : %0.2f\n", luasan);

    int hasil_balok = volume_balok (4, 5, 10);
    printf("volume_balok : %d", hasil_balok); 

    return 0;
}
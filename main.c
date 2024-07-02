#include <stdio.h>

float hitungLuasSegitiga(int alas, int tinggi){
    float luas = 0.5 * alas * tinggi;
    return luas; 
}

int main(){
    printf("halo\n");

    int a =3;
    int b = 5;

    int* pa = &a;

    printf("nilai integer adalah %d, berlokasi di pointer memori %p\n", a, pa);

    float luasan = hitungLuasSegitiga(a,b);
    printf("nilai luasan : %0.2f", luasan);

    return 0;
}
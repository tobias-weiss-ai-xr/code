/* aufg0033.c */
#include <stdio.h>
#include <string.h>

int main(void){
    char string1[5]="Bild" \
    ,string2[6]="schirm" \
    ,string3[10]="steuerung",\
    string4[19]="";

    strcat(string4,string1);
    strcat(string4,string2);
    strcat(string4,string3);
    printf("%s",string4);
}

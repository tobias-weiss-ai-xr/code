/* bspl0007.c */
#include <stdio.h>

int main(void){
  float u_faktor,betrag;
  printf("\n\tW a e r u n g s u m r e c h n e r\n");
  printf("\nBitte Umrechnungsfaktor eingeben: ");
  scanf("%f",&u_faktor);
  printf("Bitte den Euro-Betrag eingeben: ");
  scanf("%f",&betrag);
  printf("\n%.2f Euro ensprechen ",betrag);
  printf("%.2f in der Fremdwaerung.\n",betrag*u_faktor);
  return 0; 
}

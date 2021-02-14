 /* file: listing010.c
  * creator: TW
  * Last modified:  2014 Sep 12 19:33:07
  */

// tgmath.h wird verwendet, um die Dateitypen für die mathematischen Funktionen ausser Acht lassen
// zu können.

#include <stdio.h>
#include <stdlib.h>
#if __STDC_ISO_10646__ >= 19901L
  #include <tgmath.h>
#endif

int main(void)
{
  long double ldval=8.8;
  double dval=5.5, pi;
  float fval=3.3;
#if __STDC_ISO_10646__ >= 19901L
  double complex c;
#endif

  // Quadratwurzel mit reellen Zahlen
  printf("Quadratwurzel-Berechnung mit tgmath.h\n");
  printf("-------------------------------------\n");
  printf("(long double) sqrt(%Lf) = %Lf\n", ldval, sqrt(ldval));
  printf("(double) sqrt(%lf) = %lf\n", dval, sqrt(dval));
  printf("(float) double sqrt(%f) = %f\n", fval, sqrt(fval));

#if __STDC_ISO_10646__ >= 19901L
  // Berechnung mit komplexen Zahlen
  pi = 4 * atan(1.0);
  c = cexp(I * pi);
  printf("%lf + %lf * i\n", creal(c), cimag(c));
#endif
  
  return 0;
}


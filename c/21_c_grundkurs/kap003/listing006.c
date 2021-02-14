 /* file: listing006.c
  * creator: TW
  * Last modified:  2014 Sep 12 10:22:48
  */

#include <stdio.h>
#include <complex.h>

int main(void)
{
  //float f1 = 1.0;
  float complex fc = 2.0 + 3.0*I;
  //4 Bytes
  printf("sizeof(float): %lu\n", sizeof(float));
  //8 Bytes (realer und komplexer Anteil)
  printf("sizeof(float complex): %lu\n", sizeof(float complex));
  //Ausgebe vom Real- und Imaginaerteil
  printf("%f + %f\n", creal(fc), cimag(fc));
  return 0;
}


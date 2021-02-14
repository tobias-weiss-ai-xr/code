  /*
   *      p3-7.c
   *      Beispielprogramm 7, Abschnitt 3
   *      Programm zum Zaehlen von Eingabezeichen
   */

  #include <stdio.h>

  void main(void)
  {
    long nc;

    nc = 0;
    while (getchar() != EOF)
      ++nc;
    printf("%ld\n", nc);

  } /* main() */

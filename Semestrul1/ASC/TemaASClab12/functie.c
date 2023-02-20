/*++
Se citesc din fisierul numere.txt mai multe numere (pare si impare).
Sa se creeze 2 siruri rezultat N si P astfel: N - doar numere impare si P - doar numere pare. 
Afisati cele 2 siruri rezultate pe ecran.
--*/

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

// functia declarata in fisierul verificare.asm

int paritate(int num);

int main()
{
    // declaram variabilele
    int N[100], P[100];
    int i, j, verif, k, n, num,l;
    i = 0;
    j = 0;
    k = 0;
    l = 0;
    verif = 0;
    for( i=0 ; i <= 99 ; i ++)
    {
        N[i] = 0;
        P[i] = 0;
    }
    // Deschidere si citire numere din fisierul numere.txt
    FILE *fptr;
    fptr = fopen("D:\\FACULTATE\\ASC\\TemaASClab12\\numere.txt","r");
    
    if(fptr == NULL)
    {
      printf("Error!");   
      exit(1);             
    }
    
    i = 0;
    j = 0;
    n = fscanf(fptr,"%d",&num);
    while(n > 0)
    {
        //aici se obtin numerele din fisier
        //printf("%d\n", num);
        verif = paritate(num);
        if(verif == 0)
        {
            N[i] = num;
            i = i + 1;
        }
        else
        {
            P[j] = num;
            j = j + 1;
        }
        n = fscanf(fptr,"%d",&num);
    }
    
    // apelam functia scrisa in limbaj de asamblare
    /*    
        
    */
    // afisam valoarea calculata de functie
    printf("Sirul de numere impare: ");
    for(k = 0; k < i; k++)
        printf("%d ", *(N+k));
    
    printf("%c", '\n');
    printf("Sirul de numere pare: ");
    for(l = 0; l < j; l++)
        printf("%d ", *(P+l));
    
    fclose(fptr);
    return 0;
}
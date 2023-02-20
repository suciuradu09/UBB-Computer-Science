;Se da un fisier text. 
;Sa se citeasca continutul fisierului, sa se determine litera mica (lowercase) cu cea mai mare frecventa si sa se afiseze acea litera, impreuna cu frecventa acesteia.
;Numele fisierului text este definit in segmentul de date.
bits 32 


global start        

extern exit,fopen,fclose,fread,printf

import printf msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fclose msvcrt.dll             
import exit msvcrt.dll    

segment data use32 class=data
    text times 10 db 0 ; sirul in care se va citi textul din fisier
    format db "%d", 0
    
segment code use32 class=code
    start:
        
        inc byte [text + 1]
        inc byte [text + 1]
        inc byte [text + 3]
        inc byte [text + 3]
        inc byte [text + 3]
        inc byte [text + 0]
        inc byte [text + 9]
        inc byte [text + 9]
        
        
        mov edi, 0
        mov esi, text
        rep1:
            mov eax, 0
            lodsb
            
            inc edi
            cmp edi, 10
        jne rep1
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

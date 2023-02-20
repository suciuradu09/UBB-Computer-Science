;Se citest nume de fisiere pana cand apare cuvantul "end". S.s.gaseasca fisierul cu numar minim de spatii si sa se afiseze pe ecran numele fisierului si continutul lui(pe linie noua)
bits 32
global start        

extern scanf,exit
import exit msvcrt.dll    
import scanf msvcrt.dll    
segment data use32 class=data
    format_input db "%s", 0
    minim dd -1
    fis_minim times 50  db 0
    nume_fisier times 50 db 0
    end_str db "end", 0

segment code use32 class=code
    start:
        bucla:
            push nume_fisier
            push format_input
            call [scanf]
            add esp, 4 * 2
            
            mov esi, nume_fisier
            mov edi, end_str
            
            comparare:
            cmpsb
            jne prelucreaza
            cmp byte[esi], 0
            jne comparare
            cmp byte [edi], 0
            jnz prelucreaza
            je afisare
            prelucreaza:
                push dword nume_fisier
                call nr_spatii
                add esp, 4
                
                cmp eax, [minim]
                ja bucla
                mov [minim], eax
                
                mov edi, nume_fisier
                mov esi, fis_minim
                
                mov ecx, 50
                rep movsb
                jmp bucla
                AFISARE:
                push fis_minim
                call afisare_lis
                add esp, 4
                
                
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

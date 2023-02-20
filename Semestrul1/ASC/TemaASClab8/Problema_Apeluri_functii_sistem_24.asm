bits 32

global start        


extern exit,printf,scanf              
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll
;Se citesc de la tastatura doua numere a si b. 
;Sa se calculeze valoarea expresiei (a/b)*k, k fiind o constanta definita in segmentul de date.
;Afisati valoarea expresiei (in baza 2).
segment data use32 class=data
    format db "%d", 0
    amesaj db "a = ", 0
    bmesaj db "b = ", 0
    mesaj db "Valoarea expresiei (a/b)*k este: ", 0
    mesaj_eroare db "b trebuie sa fie diferit de 0", 0 
    a dw 0
    a1 dw 0
    b dw 0
    b1 dw 0
    k dw 2 
    rezultat times 33 db 0
segment code use32 class=code
    start:
        ; afisare: a = 
        push dword amesaj
        call [printf]
        add esp, 4 * 1
        
        ;citire valoare a de la tastatura
        push dword a
        push dword format
        call [scanf]
        add esp, 4 * 2
        
        ; afisare: b = 
        push dword bmesaj
        call [printf]
        add esp, 4 * 1
        
        ;citire valoare b de la tastatura
        push dword b
        push dword format
        call [scanf]
        add esp, 4 * 2
        cmp dword [b], 0
        je eroare
        
            ;afisare mesaj "Valoarea expresiei (a/b)*k este: "
            push dword mesaj
            call [printf]
            add esp, 4 * 1
            
            ;pun in EDX:EAX valoarea lui a
            mov ax, 0
            mov ax, [a]
            mov dx, 0    ; DX:AX = a
            
            div word [b] ; AX = DX:AX / [b] = a/b

            mul word [k] ; DX:AX = AX * [k]
            push dx
            push ax
            pop eax
            ;transformare in baza 2
            mov ecx, 32
            mov edi, rezultat
            mov ebx, 80000000h ; masca pentru primul bit
            repeta:
                test eax, ebx
                jnz bit1
                    
                    ; daca bitul e 0
                    mov byte [edi], '0'
                    jmp bit0 ; daca bitul e zero
                    
                bit1:
                    ;bitul e 1
                    mov byte [edi], '1'
                bit0:
                
                inc edi
                shr ebx, 1 ; se muta spre dreapta cu o pozitie toti bitii din ebx
            loop repeta
        
            ;afisare rezultat
            push rezultat
            call [printf]
            add esp, 4 * 2
        jmp final
     
        eroare: 
            push mesaj_eroare
            call [printf]
            add esp, 4 * 1
            
        final:
            push dword 0
            call [exit]
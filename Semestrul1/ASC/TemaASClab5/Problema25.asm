bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
        S1 db '+', '4', '2', 'a', '8', '4', 'X', '5'
        L1 equ $-S1
        S2 db 'a', '4', '5'
        L2 equ $-S2
        D times L1 db 0 
        ; our code starts here
segment code use32 class=code
    start:
        mov ecx, L2     ; L2 = 3
        mov esi, 0
        mov eax, 0
        mov edx, 0
        mov edi, 0
        jecxz final
        REPETA1:        
            mov ecx, L2             
            REPETA2:                    
                mov al, [S1+esi-1]  ; Se preiau elementele din siruri
                mov bl, [S2+ecx-1]  ; 
                CMP al,bl           ; al - bl => rezultat in ZF
                jz eticheta         ;Conditia pentru elemente egale din siruri diferite
            LOOP REPETA2
            mov [D+edi], al         ; Elementul valid se adauga in D
            inc edi
            eticheta:
            inc esi                 ; ESI ++
            cmp esi, L1             ; ESI - L1
        JB REPETA1                  ;sare la eticheta REPETA1 daca CF = 1
        final:
        ; Rezultat final D: '+', '2', '8', 'X'
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

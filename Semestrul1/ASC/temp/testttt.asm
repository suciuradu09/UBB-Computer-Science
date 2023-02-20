bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a1 dd -103, a6
    a2 dw 1&2, 3|4,5^6,1|2,3^4,5&6
       dw 1^2, 3&4, 5|6
    a3 dw $-$$, $$-a3
    a4 db ~((-1)^0bbh), 110bbh
    a5 dd -129<<1Fh, 81h>>0111b
    a6 dd 'a1a2a3a4a5', (a6-a5)<<(a5-a4)
    a7 times 4 dw a2, a2+1
    ;a8 dw !(a2-a1),!(a2-1)
; our code starts here
segment code use32 class=code
    start:
        ; ...
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

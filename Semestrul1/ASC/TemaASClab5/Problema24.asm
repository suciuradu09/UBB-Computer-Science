bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    A db 2, 1, -3, 0
    L1 EQU $-A
    B db 4, 5, 7, 6, 2, 1
    L2 EQU $-B
    R times L1+L2 db 0
    ;R: 1, 2, 6, 7, 5, 4, 0, -3, 1, 2
; our code starts here
segment code use32 class=code
    start:
        mov ECX, L2         ; L2 = 6
        mov EDI, 0          ;EDI = 0
        jecxz final1        
        repeta:
            mov Al, [B+ECX-1]
            mov [R+EDI], Al
            inc EDI
        loop repeta
        final1:
        ; A doua instructiune LOOP pentru sirul A
        mov ECX, L1
        jecxz final2
        repeta2:
            mov AL, [A+ECX-1]
            mov [R+EDI], AL
            inc EDI
        loop repeta2
        final2:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

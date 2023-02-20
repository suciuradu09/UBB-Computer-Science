bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
        A dw 1010h
        B dw 1100h
        C dw 1001h
        D dw 1111h
        X resq 1 

; our code starts here
segment code use32 class=code
    start:
        mov AX, [A]
        mul word[B]
        
        mov [X], AX
        mov [X+2], DX
        
        mov ax, [c]
        mul word[d]
        
        add [X], AX
        add [X+2], DX
        
        ; Rezolvare A*B + C*D
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

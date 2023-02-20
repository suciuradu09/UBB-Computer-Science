;Problema 24.
;Se da dublucuvantul M. Sa se obtina dublucuvantul MNew astfel:
;bitii 0-3 a lui MNew sunt identici cu bitii 5-8 a lui M
;bitii 4-7 a lui MNew au valoarea 1
;bitii 27-31 a lui MNew au valoarea 0
;bitii 8-26 din MNew sunt identici cu bitii 8-26 a lui M.

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
        M dd 1D5C63F7h ; 0001 1101 0101 1100 0110 0011 1111 0111b 
        MNew dd 0
        ;Rezultat :      0000 0101 0101 1100 0110 0011 1111 1111b = 055C63FFh
; our code starts here
segment code use32 class=code
    start:
        MOV EAX, [MNew]
        MOV EDX, [M]
        AND EDX, 000001E0h   ; EDX = 0000 0000 0000 0000 0000 0001 1110 0000b 
        MOV CL, 5
        SHR EDX, CL          ; EDX = 0000 0000 0000 0000 0000 0000 0000 1111b =0000000Fh 
        OR EAX, EDX          ; EAX = 0000 0000 0000 0000 0000 0000 0000 1111b =0000000Fh 
        
        OR EAX, 000000F0h;   ; EAX = 0000 0000 0000 0000 0000 0000 1111 1111b =000000FFh
        
        MOV EDX, [M]         ; Reinitializare DX
        
        AND EDX, 07FFFF00h   ; EDX = 0000 0101 0101 1100 0110 0011 0000 0000b 
        OR EAX, EDX          ; EAX = 0000 0101 0101 1100 0110 0011 1111 1111b = 055C63FFh
        
        ;Rezultat final in AX
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

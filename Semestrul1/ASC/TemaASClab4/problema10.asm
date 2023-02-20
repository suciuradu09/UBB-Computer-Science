;Problema 10
;Sa se inlocuiasca bitii 0-3 ai octetului B cu bitii 8-11 ai cuvantului A.

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
        a dw 432Ah ; 0100 0011 0010 1010b
        b db 25h   ;           0010 0101b
; our code starts here
segment code use32 class=code
    start:
        MOV AX, 0
        MOV BL, 0
        MOV AX, [a]      ; AX = 0100 0011 0010 1010b = 432Ah
        MOV BL, [b]      ; BL =           0010 0101b =   25h
        MOV CL, 8        ; CL = 08h
        SHR AX, CL       ; AX = 0000 0000 0100 0011b = 0043h
        AND BL, 11110000b; BL =      0010 0000b = 20h
        AND AX, 000Fh    ; AX = 0000 0000 0000 0011b = 0003h
        MOV BH, 0        ; BH = 0000 0000
        OR BX, AX        ; BX = 0000 0000 0010 0011b = 23h           
        
        push    dword 0      ; push the parameter for exit onto the 
        call    [exit]       ; call exit to terminate the program

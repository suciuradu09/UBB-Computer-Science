;Problema 13.
;Dandu-se 4 octeti, sa se obtina in AX suma numerelor intregi ;reprezentate de bitii 4-6 ai celor 4 octeti.

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
        a db 7Ah ; 0111 1010b
        b db 2Fh ; 0010 1111b
        c db 61h ; 0110 0001b
        d db 2Eh ; 0010 1110b
        ;Rezultat final: 17 = 11h = 0001 0001b

segment code use32 class=code
    start:
        MOV AX,0 ; AX = 0000h
        MOV AL, [a] ; AL = 7Ah = 0111 1010b
        MOV BX,0 ; BX = 0000h
        MOV BL, [b] ; BL = 2Fh = 0010 1111b
        MOV CX,0 ; CX = 0000h
        MOV CL, [c] ; CL = 61h = 1110 0001b
        MOV DX,0 ; DX = 0000h
        MOV DL, [d] ; DL = 2Eh = 0010 1110b
        
        AND AL, 70h ; AL = 0111 0000b = 70h
        AND BL, 70h ; BL = 0010 0000b = 20h
        AND CL, 70h ; CL = 0110 0000b = 60h
        AND DL, 70h ; DL = 0010 0000b = 20h
        
        SHR AL, 4 ; AL = 0000 0111b = 07h
        SHR BL, 4 ; BL = 0000 0010b = 02h
        SHR CL, 4 ; CL = 0000 0110b = 06h
        SHR DL, 4 ; DL = 0000 0010b = 02h
        
        ADD AX, BX; AX = AX + BX = 09h
        ADD AX, CX; AX = AX + CX = 0Fh
        ADD AX, DX; AX = AX + DX = 11h
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

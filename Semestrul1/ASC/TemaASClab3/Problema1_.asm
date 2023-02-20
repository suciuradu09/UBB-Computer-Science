;Adunari si scaderi - problema 24 - cu semn
;((a + b) + (a + c) + (b + c)) - d
;a - byte, b - word, c - double word, d - qword
;((-2 + 5) + (-2 + 9) + (5 + 9)) - 3 = (3 + 7 + 14) - 3 = 24 - 3 = 21 = 0001 0101b= 15h 
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
        a db -2
        b dw 5
        c dd 9
        d dq 3
        r resq 1 ; Rezerv un quadword in memorie pentru rezultat
; our code starts here
segment code use32 class=code
    start:
        mov AL, [a] ;AL = a = -2
        cbw         ;AL -> AX = a = -2
        mov DX, [b] ;DX = b = 5
        add DX,AX   ;DX = DX + AX = a + b = -2 + 5 = 3
        
        cwde        ;EAX = AX = a = 3
        mov EBX, [c];EBX = c = 9
        add EBX,EAX ;EBX = EBX + EAX = c + a = 9 + (-2) = 7
        
        mov EAX ,0  
        mov AX,DX   ;AX = DX = a + b = 3 = 3h
        cwde        ;EAX = AX = a + b = 3 = 3h
        
        add EAX, EBX;EAX = EAX + EBX = (a + b) + (a + c) = 3 + 7 = 10
        
        mov EBX, EAX;EBX = EAX = (a + b) + (a + c) = 10
        
        mov EAX, 0  ;EAX = 0000 0000 0000 0000 0000 0000 0000 0000b
        mov AX, [b] ;AX = b = 5
        cwde        ;EAX = AX = b = 5
        mov EDX, 0  ;EDX = 0000 0000 0000 0000 0000 0000 0000 0000b
        mov EDX,[c]  ;EDX = c = 9
        add EDX,EAX ;EDX = EDX + EAX = b + c = 5 + 9 = 14
        
        mov EAX, 0  ;EAX = 0000 0000 0000 0000 0000 0000 0000 0000b
        add EAX,EBX ;EAX = EAX + EBX = (a + b) + (a + c) = 10 = A
        add EAX,EDX ;EAX = EAX + EDX = (a + b) + (a + c) + (b + c) = 10 + 14 = 24 = 18h
        
        cdq         ;EDX:EAX = EAX = (a + b) + (a + c) + (b + c) = 24 = 18h
        
        ; d -> EBX:ECX
        mov ECX, dword[d+0] ; 00 03h
        mov EBX, dword[d+4] ; 00 00h
        ;EBX:ECX = 00 00 00 03 h
        ;((a + b) + (a + c) + (b + c)) - d
        ; EDX : EAX -
        ; EBX : ECX
        clc ; clear carry flag (CF = 0)
        sub EAX, ECX ; EAX = EAX - ECX       00 18h - 00 03h
        sbb EDX, EBX ; EDX = EDX - EBX - CF  00 00h - 00 00h
        ;              EDX : EAX = 00 00 00 15h
        mov dword [r+0], EAX 
        mov dword [r+4], EDX 
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

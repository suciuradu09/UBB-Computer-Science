;Adunari si scaderi - problema 24 - fara semn
;(a + b + c) - d + (b - c)
;a - byte, b - word, c - double word, d - qword
; 
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
        a db 8
        b dw 4
        c dd 3
        d dq 1
        r resq 1 ; Rezerv un quadword in memorie pentru rezultat
; our code starts here
segment code use32 class=code
    start:
        mov AL, [a] ; AL = a = 8 = 8h
        mov BX, [b] ; BX = b =  4 = 4h
        mov ECX,[c] ; ECX = c = 3 = 3h
        mov AH, 0 ; AL - > AX = a = 8 = 8h
        add AX, BX  ; AX = AX + BX = a + b = 8 + 4 = 12 = Ch
        mov DX, 0 ; AX - > DX:AX = a + b = 12 = Ch
        ;CX:BX = c
        mov BX, word[c+0]
        mov CX, word[c+4]
        ;DX:AX+
        ;CX:BX
        add DX, CX ;DX = DX + CX
        add AX, BX ;AX = AX + BX
        ;DX:AX = a + b + c = 12 + 3 = 15 = Fh
        
        ;DX:AX -> EDX:EAX = a + b + c = 15 = Fh
        
        mov EBX, dword[d+0]
        mov ECX, dword[d+4]
        ; ECX : EBX = d = 1 
        
        ; EDX : EAX -
        ; ECX : EBX
        ; (a + b + c) - d = 15 - 1 = 14 = Eh
        sub EAX, EBX ;EAX = EAX - EBX 
        sbb EDX, ECX ;EDX = EDX - ECX
        
        mov ECX, EDX
        mov EBX, EAX 
        ;EDX : EAX -> ECX : EBX = (a + b + c) - d = 14 = Eh
        
        mov AX, [b] ; AX = b = 4 = 4h
        mov DX,0    ; AX -> DX:AX = b = 4 = 4h
        ;DX:AX - [c]
        sbb AX, word[c]; AX = AX - c - CF =  b - c = 4 - 3 = 1 = 1h
        
        ;DX:AX -> EDX:EAX = b - c = 5
        
        clc ; CF = 0
        add EBX, EAX ;EBX = EBX + EAX 
        adc ECX, EDX ;ECX = ECX + EDX + CF 
        ;ECX : EBX = (a + b + c) - d + (b - c) = 14 + 1 = 15 = Fh
        
        mov dword[r+0], EBX  
        mov dword[r+4], ECX
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

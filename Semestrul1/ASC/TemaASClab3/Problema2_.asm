;Adunari si scaderi - problema 24 - cu semn
;(a + b + c) - d + (b - c)
;a - byte, b - word, c - double word, d - qword
;(-9 + 8 + (-3)) - 6 + (8 - (-3)) = -4 - 6 + 11 = -10 + 11 = 1 = 00 00 00 01h
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
        a db -9
        b dw 8
        c dd -3
        d dq 6
        r resq 1 ; Rezerv un quadword in memorie pentru rezultat
; our code starts here
segment code use32 class=code
    start:
        mov AL, [a] ; AL = a = -9 
        mov BX, [b] ; BX = b =  8
        mov ECX,[c] ; ECX = c = -3
        cbw ; AL - > AX = a = -9 
        add AX, BX  ; AX = AX + BX = a + b = -9 + 8 = -1
        cwde ; AX - > EAX = -1
        add EAX, ECX ; EAX = EAX + ECX = -1 +(-3) = a + b + c = -4
        cdq 
        ; EDX : EAX  = 00 00 00 03h
        
        mov EBX, dword[d+0]
        mov ECX, dword[d+4]
        ; ECX : EBX = d
        
        ; EDX : EAX -
        ; ECX : EBX
        ; (a + b + c) - d
        clc ; clear carry flag
        sub EAX, EBX ;EAX = EAX - EBX = 00 03h - 00 06h = 00 0Ah 
        sbb EDX, ECX ;EDX = EDX - ECX - CF
                
        mov ECX, EDX
        mov EBX, EAX 
        ;EDX : EAX -> ECX : EBX = (a + b + c) - d = -10
        
        mov AX, [b] ; AX = b = 8
        cwde        ; AX -> EAX = b = 8
        sub EAX, dword[c]; EAX = EAX - c = b - c = 8 - (-3)= 11 = Bh
        cdq
        ;EAX - > EDX : EAX = b - c = 11
        clc ; CF = 0
        add EBX, EAX ;EBX = EBX + EAX 
        adc ECX, EDX ;ECX = ECX + EDX + CF 
        ;ECX : EBX = (a + b + c) - d + (b - c) = -10 + 11 = 1 = 1h
        
        mov dword[r+0], EBX  
        mov dword[r+4], ECX
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

;Înmulțiri, împărțiri - problema 24 - cu semn
;a-(7+x)/(b*b-c/d+2); 
;a-doubleword; b,c,d-byte; x-qword
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
        a dw 10
        b db 2
        c db 4
        d db -2
        x dq 9
        r resw 1 ; Rezerv un word in memorie pentru rezultat
; our code starts here
segment code use32 class=code
    start:
        
        mov AL, [b]  ; AL = b
        imul byte[b]; AX = AL * byte b = b * b = 2 * 2 = 4
        mov BX, AX  ; BX = AX = b*b = 4
        
        mov AX, 0
        mov AL, byte[c] ; AL = c = 5
        cbw             ; AL -> AX = c
        idiv byte[d]    ; AL = AX/byte[d] = c/d = 4/-2 = -2
        cbw             ; AL -> AX = c/d = -2
        sub BX, AX      ; BX = BX - AX = b * b - c / d = 4 - (-2) = 6 = 6h
        add BX, 2       ; BX = BX + 2 = b * b - c / d + 2 = 6 + 2 = 8 = 8h
        
        ; EDX:EAX = x - qword
        
        mov EAX, dword[x+0]
        mov EDX, dword[x+4]
        
        adc EAX, 7      ; EDX : EAX = EDX : EAX + 7 = X + 7 = 9 + 7 = 16 = 10h
        
        idiv BX         ; AX = EAX/BX= (x + 7)/(b * b - c / d + 2) = 16 / 8 = 2 = 2h
        
        mov BX, 0
        mov BX, [a]     ;BX = a
        
        sub BX, AX      ;BX = BX - AX = 10 - 2 = 8 = 8h

        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

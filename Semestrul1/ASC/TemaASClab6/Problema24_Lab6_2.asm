bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
        s1 dd 1010b , 1100b, 1011b
        LS1 EQU ($-s1)/4
        R times LS1 dd 0
        doi dw 2
; our code starts here
segment code use32 class=code
    start:
        mov ECX, LS1
        mov ESI, s1+4*(LS1-1)
        mov EDI, R
        std     ;DF = 1

        jecxz  final
        repeta:
            mov EBX, 0
            LODSD ; EAX = DS:[ESI], ESI= ESI - 4
            push EAX
            repeta2:
                push ECX
                mov DX, 0
                mov CX, 2
                div CX ; AX = DX:AX / doi | DX = EAX % doi
                cmp DX, 0 ; Verifica daca restul este 1 sau 0
                pop ECX
                jnz aici
                    INC EBX ; daca ZF = 1
                aici:
                cmp AX, 0
            jnz repeta2 ; cat timp catul este diferit de 0
            MOV EAX, 0
            MOV EAX, EBX
            div word[doi] ; DX = DX:AX % 2
            cmp DX, 0
            jnz daca
                POP EAX
                cld
                STOSD ; ES:[EDI] = EAX
            daca:
            std
        LOOP repeta
        final:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

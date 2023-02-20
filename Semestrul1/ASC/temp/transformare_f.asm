bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start      
global transformare

; declare external functions needed by our program
extern exit,printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; sir db '234', 0
    ; len equ $-sir
    ; format db "%d", 0
    
    
; our code starts here
segment code use32 class=code
    transformare:
    ; esp-adresa de revenire
    ; esp+4-adresa sir
    ; esp+8-valoare len
        
        mov ecx, [esp+8]
        dec ecx
        mov ebx, 1
        mov edx, 0
        mov esi, [esp+4]
    repeta:
        mov eax, 0
        mov al, [esi+ecx-1]
        sub al, '0'
        mul bl
        add edx, eax
        mov al, bl
        mov bl, 10
        mul bl
        mov ebx,eax
        
        
        loop repeta
        ret
        
    ; start:
    
        ; push dword len
        ; push dword sir
        ; call transformare
        ; add esp, 4*2
            
        ; push dword edx
        ; push dword format
        ; call [printf]
        ; add esp ,4*2
        
    
        ; ; exit(0)
        ; push    dword 0      ; push the parameter for exit onto the stack
        ; call    [exit]       ; call exit to terminate the program

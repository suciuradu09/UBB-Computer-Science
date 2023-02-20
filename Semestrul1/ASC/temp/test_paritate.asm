bits 32
global start

import printf msvcrt.dll
import exit msvcrt.dll
extern printf, exit

segment data use32
        format_string db "%d",0
segment code use32 public code
start:
    mov eax, 0
    mov eax, 9
    
    
    mov ebx, 0
    
    test eax, 1
    jz even_number
    ;odd number 
    mov ebx, 1
   
   even_number:
	
    
    cmp ebx, 0
    je aici
    
    push eax
	push format_string
	call [printf]
	add esp, 2*4

    aici:
	push 0
	call [exit]

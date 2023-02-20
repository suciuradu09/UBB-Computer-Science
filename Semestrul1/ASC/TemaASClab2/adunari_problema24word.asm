; Adunări și scăderi - problema 24
; (a-c)+(b-d)
bits 32 

global  start 

extern  exit 
import  exit msvcrt.dll
        
segment  data use32 class=data 
	a dw 10 ; declar o variabila de tip word
	b dw 7  ; declar o variabila de tip word
    c dw 8  ; declar o variabila de tip word
    d dw 5  ; declar o variabila de tip word
segment  code use32 class=code
start: 

	MOV AX, [a]; AL = a
    SUB AX, [c]; AL = a - c
    
    MOV DX, [b]; DL = b
    SUB DX, [d]; DL = b - d
    
    ADD AX,DX ; AX = ( a - c ) + ( b - d )
    
	push   dword 0 
	call   [exit]
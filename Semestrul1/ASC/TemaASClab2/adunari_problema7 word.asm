; Adunări și scăderi - problema 7
; (c+c+c)-b+(d-a)
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

	MOV AX, [c]; AL = c
    ADD AX, [c]; AL = c + c
    ADD AX, [c]; AL = c + c + c
    SUB AX, [b]; AL = (c + c + c) - b
    
    MOV DX, [d]; DL = d
    SUB DX, [a]; DL = d - a
    
    ADD AX,DX ; AX = (c + c + c) - b + (d - a)
    
	push   dword 0 
	call   [exit]
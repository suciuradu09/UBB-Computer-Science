; Adunări și scăderi - problema 24
; (a-b-b-c)+(a-c-c-d)
bits 32 

global  start 

extern  exit 
import  exit msvcrt.dll
        
segment  data use32 class=data 
	a db 10 ; declar o variabila de tip byte
	b db 7  ; declar o variabila de tip byte
    c db 8  ; declar o variabila de tip byte
    d db 5  ; declar o variabila de tip byte
segment  code use32 class=code
start: 

	MOV AL,  [a]; AL = a
    SUB AL,  [b]; AL = AL - b/ AL = a - b
    SUB AL,  [b]; AL = a - b - b
    SUB AL,  [c]; AL = a - b - b - c
    
    MOV DL, [a]; DL = a
    SUB DL, [c]     ; DL = a - c
    SUB DL, [c]     ; DL = a - c - c
    SUB DL, [d]     ; DL = a - c - c - d
    
    ADD AL,DL ; AL = (a - b - b - c) + (a - c - c - d)
    
	push   dword 0 
	call   [exit]
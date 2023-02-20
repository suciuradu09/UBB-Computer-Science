; Adunări și scăderi - problema 7
; c-(d+d+d)+(a-b)
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

	MOV AL, [c] ;AL = c
    MOV DL, [d] ;DL = d
    ADD DL, [d] ;DL = d + d
    ADD DL, [d] ;DL = d + d + d
    SUB AL, DL  ;AL = AL - DL / c - (d + d + d)
    MOV DL, [a];DL = a
    SUB DL, [b];DL = DL - b / DL = a - b
    ADD AL, DL  ;AL = c - (d + d + d) + (a - b)
	push   dword 0 
	call   [exit]
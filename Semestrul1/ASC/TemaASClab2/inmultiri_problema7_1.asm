; Înmulțiri și împărțiri - problema 7
; [100*(d+3)-10]/d
bits 32 

global  start 

extern  exit 
import  exit msvcrt.dll
        
segment  data use32 class=data 
    d dw 2  ; declar o variabila de tip word
    
segment  code use32 class=code
start: 
    MOV AX, 100     ; AX = 100
    ADD [d], 3      ; d = d + 3
    MUL word[d]     ; DX:AX = AX * d -> (d+3)*100
    SUB AX, 10      ; AX = AX - 10 -> 100*(d+3)-10
    DIV word[d]     ; AX = DX:AX / d -> [100*(d+3)-10]/d
    
	push   dword 0 
	call   [exit]
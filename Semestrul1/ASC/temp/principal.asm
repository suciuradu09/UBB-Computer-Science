bits 32 

global start

extern exit, printf

%include "ceva.asm"

import exit msvcrt.dll  
import printf msvcrt.dll  
   
segment data use32 class=data public
      sir dd 0x12345678,-1, 25634, 28252h, 24252o, 01010100y, 23o
      lungime equ ($-sir)/4
      suma dd 0
      format db "%d  ", 0
      d times 100 dd 0
segment code use32 class=code public
    start:
        mov esi, sir
        mov edi, d
        mov eax, 0
        mov edx, lungime
        repet1:
            
            lodsd
            pushad
            call modul
            ;rezultat in edx
            
            mov dword [suma], edx
            
            popad
            pushad
            
            push dword [suma]
            push dword format
            call [printf] 
            add esp, 4*2
            
            popad
            mov dword[suma], 0
            
        dec edx
        cmp edx, 0
        jne repet1
        
        
        
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

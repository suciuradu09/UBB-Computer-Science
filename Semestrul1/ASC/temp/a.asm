bits 32

global start        

extern exit, printf,start2              

import exit msvcrt.dll
import printf msvcrt.dll
import start2 b.asm

%include "b.asm"

segment data use32 class=data public
    sir dd -1,123456,0xabcdeff

    
segment code use32 class=code public
    start:
        
    
        
        push    dword 0     
        call    [exit]       
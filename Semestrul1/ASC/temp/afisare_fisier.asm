bits 32
global afisare_fisier

extern exit, printf    
import exit msvcrt.dll

segment data use32 class=data
    mod_acces db "r", 0
    descriptor dd -1 
    newline db 10, 13, 0
segment code use32 class=code
    afisare_fisier:
        mov edx, [esp + 4]
        ;printf(%s, text)
        push edx
        call [printf]
        add esp, 4 * 1
        
        
        push    dword 0      
        call    [exit]      
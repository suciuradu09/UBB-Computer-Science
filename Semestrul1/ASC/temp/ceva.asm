bits 32

global modul        

    modul:
        
        mov ebx, 0
        mov edx, 0
        mov ecx, 8
        repeta:
            mov bl, al
            shl bl, 4
            shr bl, 4
            add dl, bl
            shr eax, 4
        loop repeta
        ;edx rezultat
    ret
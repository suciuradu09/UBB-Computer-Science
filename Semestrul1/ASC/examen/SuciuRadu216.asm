bits 32 
global start        

extern exit, fscanf, fopen, fclose, printf, fprintf             
import exit msvcrt.dll    
import fscanf msvcrt.dll    
import fopen msvcrt.dll    
import fclose msvcrt.dll    
import printf msvcrt.dll    
import fprintf msvcrt.dll    

segment data use32 class=data
    sir db "1234567890",0
    nume_fisier db "input.txt",0
    n db 0
    format_s db "%s", 0
    format_d db "%d", 0
    mod_acces db "r",0
    mod_acces_fisier db "w", 0
    descriptor_fisier dd -1
    nume_fisier_creat db  "output-0.txt", 0
    sir_scris times 15 db 0
    descriptor_afisare dd -1
    format db "%s", 0
    sir_gol dd "", 0
segment code use32 class=code
    start:
        
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor_fisier], eax
        cmp eax, 0
        je final
        
        ;Citire numar din fisier
        push dword n
        push dword format_d
        push dword [descriptor_fisier]
        call [fscanf]
        add esp, 4 * 2
        ;//
        
        mov ecx, 0
        mov ecx, [n]
        
        mov ebx, 0
        mov bl, 7
        
    repeta:
        mov esi, sir
        mov edi, sir_scris
        push ecx
        mut:
            movsb
            dec ecx
            cmp ecx, -1
        jne mut
        pop ecx
        
        ;Creez n fisiere
        mov esi, nume_fisier_creat
        add ecx, 48
        mov [esi + ebx], cl
        sub ecx, 48
        
        push ecx
        
        push dword mod_acces_fisier
        push dword nume_fisier_creat
        call [fopen]
        add esp, 4 * 2
        ;Descriptor in EAX
        mov [descriptor_afisare], eax
        
        
        push dword sir_scris
        push dword format
        push dword [descriptor_afisare]
        call [fprintf]
        add esp, 4 * 3
        
        mov edx, 10
        mov edi, sir_scris
        golire:
            mov byte[edi + edx], 0
            dec edx
            cmp edx, -1
        jne golire

        
        pop ecx
        dec ecx
        cmp ecx, -1
        jne repeta
        
        
        ;Inchidere fisier
        push dword [descriptor_fisier]
        call [fclose]
        add esp, 4
        
    final:
        push    dword 0      
        call    [exit]      

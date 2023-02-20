;;Sa se citeasca de la tastatura un nume de fisier si un numar. 
;Sa se citeasca din fisierul dat cuvintele separate prin spatii si sa se afiseze in consola numai cuvintele
;a caror numar de vocale este egal cu numarul citit de la tastatura.
bits 32 
global start        

extern exit, printf, scanf,fscanf, fclose, fopen
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll
import fscanf msvcrt.dll
import fclose msvcrt.dll
import fopen msvcrt.dll

segment data use32 class=data
    descriptor dd -1
    format_s db "%s",0
    format_s_afisare db "%s", 32 ,0
    format_afisare db "Introduceti numele fisierului: ",0
    mod_acces db "r",0
    nume_fisier times 20 db 0
    cuvant times 20 db 0
    
segment code use32 class=code
    start:
        push dword format_afisare
        call [printf]
        add esp, 4
        
        push dword nume_fisier
        push dword format_s
        call [scanf]
        add esp, 4 * 2
        
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor], eax
        
        cmp eax, 0
        je final
        
        push dword cuvant
        push dword format_s
        push dword [descriptor]
        call [fscanf]
        add esp, 4 * 3
        
        
        repeta:
        
        push dword cuvant
        push dword format_s_afisare
        call [printf]
        add esp, 4 * 2
         
        push dword cuvant
        push dword format_s
        push dword [descriptor]
        call [fscanf]
        add esp, 4 * 3
         
                
        cmp eax, 1
        
        je repeta
        
        push dword [descriptor]
        call [fclose]
        add esp, 4
        
        final:
    
        push    dword 0      
        call    [exit]      

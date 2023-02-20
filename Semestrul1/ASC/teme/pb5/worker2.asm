;Se citeste de la tastatura un nume de fisier, un caracter special s (orice caracter in afara de litere si cifre)
;si un numar n reprezentat pe octet.
;Fisierul contine cuvinte separate prin spatiu. Sa se scrie in fisierul output.txt ultimele n caractere din fiecare cuvant.
;(Daca numarul de caractere al cuvantului este mai mic decat n, cuvantul se va prefixa cu caracterul special s).

bits 32 
global start        

extern exit, printf, scanf,fscanf, fclose, fopen, fprintf
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll
import fscanf msvcrt.dll
import fclose msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll

segment data use32 class=data
    descriptor dd -1
    descriptor_out dd -1
    
    format_s db "%s",0
    format_d db "%d",0
    format_c_s db "%s %d", 0
    format_s_afisare db "%s", 32 ,0
    format_afisare db "Introduceti numele fisierului: ",0
    format_afisare_c db "Introduceti caracterul special si n: ", 0
    nume_fisier_out db "output.txt", 0
    n dd 0
    c db 0
    mod_acces db "r",0
    mod_scriere db "w", 0
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

        ; Deschidere fisier
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor], eax
        
        cmp eax, 0
        je final
        
        push dword mod_scriere
        push dword nume_fisier_out
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor_out], eax
        
        push dword cuvant
        push dword format_s
        push dword [descriptor]
        call [fscanf]
        add esp, 4 * 3
        
        
        repeta:
        push dword cuvant
        push dword format_s_afisare
        push dword [descriptor_out]
        call [fprintf]
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
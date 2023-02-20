bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fread, fprintf, printf, fclose           ; tell nasm that exit exists even if we won't be defining it
extern transformare
extern invers_transformare
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    nume_fis db "numere.txt", 0   ; numele fisierului care va fi deschis
    mod_acces db "r", 0          ; modul de deschidere a fisierului - 
                                 ; r - pentru scriere. fisierul trebuie sa existe 
    descriptor_fis dd -1         ; variabila in care vom salva descriptorul fisierului - necesar pentru a putea face referire la fisier
    len equ 10                     ; numarul maxim de elemente citite din fisier.                            
    text times len dd 0          ; sirul in care se va citi textul din fisier 
    ft db "%s", 0
    aux times 4 db 0
    cifre_citite times 3 db 0
    N times 10 db 0
    P times 10 db 0
    i db 0
    j db 0

    

; our code starts here
segment code use32 class=code
    start:
        ; apelam fopen pentru a deschide fisierul
        ; functia va returna in EAX descriptorul fisierului sau 0 in caz de eroare
        ; eax = fopen(nume_fisier, mod_acces)
        push dword mod_acces
        push dword nume_fis
        call [fopen]
        add esp, 4*2                ;eliberam parametrii de pe stiva
        
        mov [descriptor_fis], eax   ; salvam valoarea returnata de fopen in variabila descriptor_fis
        
        ; verificam daca functia fopen a creat cu succes fisierul (daca EAX != 0)
        cmp eax, 0                      
        je final                        ; daca citirea din fisier nu are succes
        
        ; citim textul in fisierul deschis folosind functia fread
        ; eax = fread(text, 1, len, descriptor_fis)
        push dword [descriptor_fis]
        push dword len
        push dword 1
        push dword text        
        call [fread]
        add esp, 4*4                 ; dupa apelul functiei fread EAX contine numarul de caractere citite din fisier
       
        mov esi, text
        mov ecx, eax
        cld
        mov ebx, 0
       
        repeta:
            lodsb
            cmp al, " "
            jne continua
            push ecx
                
            push ebx
            push dword aux 
            call transformare   ;edx=numar
            
            add esp, 4*2
            pop ecx
            
            test edx, 1b
            jz par
                push edx
                call invers_transformare
                mov edx, eax
                mov eax, [i]
                mov [eax+N],edx
                inc eax
                mov [i],eax
                jmp reset
            
            par:
                push edx
                call invers_transformare
                mov edx, eax
                mov eax, [j]
                mov [eax+P],edx
                inc eax
                mov [j],eax
            
            reset:
                mov ebx,0
                jmp peste
            continua:
                mov [aux+ebx], al
                inc ebx
            peste:
            loop repeta
    
    push dword P
    push dword ft
    call [printf]
    add esp,4*2
    
    push dword N
    push dword ft
    call [printf]
    add esp,4*2
    
    
    
    final:
    
    push dword [descriptor_fis]
    call [fclose]
    add esp,4
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

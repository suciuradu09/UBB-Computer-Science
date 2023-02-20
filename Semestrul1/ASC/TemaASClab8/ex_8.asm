bits 32 
global start   
extern exit, fopen, fread, fprintf, printf, fclose            
import exit msvcrt.dll    
import fopen msvcrt.dll
import fread msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll

;Se da un fisier text. Sa se citeasca continutul fisierului, 
;sa se determine litera mare (uppercase) cu cea mai mare frecventa 
;si sa se afiseze acea litera, impreuna cu frecventa acesteia. 
;Numele fisierului text este definit in segmentul de date.

segment data use32 class=data
    nume_fisier db "a.txt", 0   ; numele fisierului care va fi deschis
    mod_acces db "r", 0          ; modul de deschidere a fisierului - 
                                 ; r - pentru scriere. fisierul trebuie sa existe 
    descriptor_fis dd -1         ; variabila in care vom salva descriptorul fisierului - necesar pentru a putea face referire la fisier
    len equ 100                  ; numarul maxim de elemente citite din fisier.                            
    text times len db 0          ; sirul in care se va citi textul din fisier 
    nr_citite dd 0               ;cate caractere s-au citit din fisier
    frecventa times 26 dd 0        ;vectorul de frecventa pe litere
    max dd 0                     ;numarul maxim de aparitii al unei cifre citite
    litera dd 0               ;majuscula cu numarul maxim de aparitii
    format_afisare dd "Majuscula cu cea mai mare frecventa este %c, iar frecventa acesteia este %d", 0
    format db "%d",0
segment code use32 class=code
    start:    
        ; apelam fopen pentru a deschide fisierul
        ; functia va returna in EAX descriptorul fisierului sau 0 in caz de eroare
        ; eax = fopen(nume_fisier, mod_acces)
        push dword mod_acces
        push dword nume_fisier
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
        
        mov [nr_citite],eax          ;pt ca in eax e numarul de caractere citite din fisier
        mov ecx,[nr_citite]
        mov esi, text
        cld

        
        ;vector de frecventa
        repeta_1:
            lodsb                   ;in AL este caracterul pe care il verificam daca e majuscula
            cmp al, 65              
            jb nu_e_maj
            cmp al, 90
            ja nu_e_maj
            sub al, 65 
            cbw
            cwde
            mov edi, eax            
            add dword [frecventa + edi], 1  
                push dword [frecventa + edi]
                push dword format
                call [printf]
                add esp, 4 * 2
            nu_e_maj:
        loop repeta_1
        
        mov ecx, 26                  ; lungimea vectorului de frceventa = numarul de majuscule
        mov edi ,0
        
        
        ;determinam majuscula cu frecventa maxima
        repeta_2:
            mov ebx, [max]
            cmp ebx, [frecventa+edi]
            jb nu_e_mai_mare
            ;inc edi
            mov al,[frecventa+edi]
            mov [max], al
            mov edx, edi
            add edx, 65
            mov [litera], edx   ;litera = majuscula cu nr max de aparitii
            inc edi
            nu_e_mai_mare:
            loop repeta_2
            
         mov ecx, 26                  ; lungimea vectorului de frceventa=numarul de majuscule
         mov ebx , 0                 ; initializam numarul de aparitii al majusculei cu frecventa maxima cu 0
         mov edi, 0

        ;determinam numarul de aparitii al majusculei cu frecventa maxima
        repeta_3:
            mov edx, [max]
            cmp edx, [frecventa+edi]
            inc edi
            jne nu_sunt_egale
            add ebx, 1
        
            nu_sunt_egale:
            loop repeta_3
                    
        ;afiseaza cifra cu frecvenat maxima si numarul de aparitii ale acesteia
        push dword [max]
        push dword [litera]
        push dword format_afisare
        call [printf]
        add esi, 4*3
        
        ; apelam functia fclose pentru a inchide fisierul
        ; fclose(descriptor_fis)
        push dword [descriptor_fis]
        call [fclose]
        add esp, 4
        
        
        
        final:
        
        ; exit(0)
        push    dword 0      
        call    [exit]     
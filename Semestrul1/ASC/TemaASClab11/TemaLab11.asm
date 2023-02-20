; Se citesc din fisierul numere.txt mai multe numere (pare si impare). 
; Sa se creeze 2 siruri rezultat N si P astfel: N ;- doar numere impare si P - doar numere pare. 
; Afisati cele 2 siruri rezultate pe ecran.
bits  32
global  start
import  printf msvcrt.dll
import  fopen msvcrt.dll
import  fclose msvcrt.dll
import  fread msvcrt.dll
import  exit msvcrt.dll
extern  printf, exit, fopen, fread, fclose

%include "transformare.asm"
%include  "reversed_transformare.asm"

segment  data use32 public data
    nume_fisier db "numere.txt", 0
    mod_acces db "r", 0
    descriptor_fis dd -1
    format_afisare1 db "Sirul cu numere pare: %s", 0
    format_afisare2 db "Sirul cu numere impare: %s", 0
    len equ 100
    text times len db 0
    nr_car_citite dd 0
    s1 times len db 0
    s2 times len db 0
    endline db 10, 0
    formats db "%s", 0
    sir_numar times 4 db 0
    nr_caractere dd 0
    sir times 10 db 0
    aux times 100 db 0
    i db 0
    j db 0
segment  code use32 public code
start:
    ;DESCHIDERE FISIER
    push dword mod_acces
    push dword nume_fisier
    call [fopen]
    add esp, 4*2
    
    cmp eax, 0
    je final
    
        mov [descriptor_fis], eax
        push dword [descriptor_fis]
        push dword len
        push dword 1
        push dword text
        call [fread] ;se citestc maxim 100 de caractere din sir
        add esp, 4 * 4      

        mov [nr_car_citite], eax
        
        mov ecx, [nr_car_citite] ; Numarul de repetari efectuate
        mov esi, text
        
        mov ebx, 0
   ;CITIRE NUMERE DIN FISIER
   repeta_citire:
       lodsb  ;al = [esi + x]
       cmp al, " "
       jne e_Caracter
            ; daca nu e caracter se face transformarea
            push ecx 
            mov ecx, ebx
            sub ecx, dword[nr_caractere]
            mov dword[nr_caractere], ecx
            
            ;transformare(sir, nr_caractere)
                    push ebx
                    push dword aux
                    call transformare ;rezultat in edx
                    add esp, 4 * 2
     
            ;verificare paritate
            test edx,1           ; mask-out all bit except the lowest one
            
            jz   even_value     ; when lowest bit is zero, value is even
                ; odd value
                push dword [nr_caractere]
                push dword sir
                push edx
                call reversed_transformare
                add esp, 4 * 3
                mov edx, eax
                mov eax, [j]
                mov [s2 + eax],edx
                inc eax
                mov [j], eax
                jmp again
            even_value:
                push dword [nr_caractere]
                push dword sir
                push edx
                call reversed_transformare
                add esp, 4 * 3
                mov edx, eax
                mov eax, [i]
                mov [s1 + eax],edx
                inc eax
                mov [i], eax
            again:
                mov ebx, 0
                jmp sari
       e_Caracter:
            mov [aux + ebx], al
            inc ebx
       sari:
       ;curatare sir 
       ;mov ecx, 10
       ;curatare:
       ;     mov byte[sir+ecx-1], 0
       ;     dec ecx
       ;     cmp ecx, 0
       ;jne curatare
       pop ecx
       loop repeta_citire
   
   
   ;AFISARE
    push s1
    push format_afisare1
    call [printf]
    add esp, 4 * 2
    
    push dword endline
    push dword formats
    call [printf]
    add esp, 4 * 2
    
    push s2
    push format_afisare2
    call [printf]
    add esp, 4 * 2
    
   ;inchidere fisier
   push dword [descriptor_fis]
   call [fclose]
   add esp, 4
        
    final:
    
	push 0
	call [exit]
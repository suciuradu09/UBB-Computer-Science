bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fread, fprintf, printf, fclose             ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
        fis db 'prob17.txt',0
        len equ 120
        text times len db 0
        mod_acces db "r",0
        descript dd -1
        formatcitire db "%s",0
        formatafisare db "Litera %c apare de %d ori",0
        litere_mari times 26 dd 0
        actread dd 0;cate caractere a citit
        max dd 0
;Se da un fisier text. Sa se citeasca continutul fisierului, sa se determine litera mare (uppercase) cu cea mai mare frecventa si sa se afiseze acea litera, impreuna cu frecventa acesteia. Numele fisierului text este definit in segmentul de date.
segment code use32 class=code
    start:
        push dword mod_acces
        push dword  fis
        call [fopen]
        add esp,4*2
        
        mov [descript],eax
        cmp dword [descript],0
        je final
        
        
        ;fread(text,1,len,descript)
        push dword[descript]
        push dword len
        push dword 1;citesc un octet 
        push text
        call [fread]
        add esp, 4*4
        
        mov [actread],eax;pt ca in eax e numarul caracterelor citite
        
        push dword [descript]
        call [fclose]
        add esp,4*1
        
        mov ecx,[actread]
        mov esi, text
        cld
        
        ;litere_mari este vector de frecventa
        repeta:
            mov eax, 0
            lodsb
            cmp al, 97
            jb nu_e_litera_mare
            sub al, 97 
            inc dword [litere_mari + eax]
            nu_e_litera_mare:
            loop repeta
        
        mov ecx, 26
        
        repeta2:
            mov eax,[max]
            cmp  eax, [litere_mari+ecx]
            jb nu_e_mai_mare
            mov eax,[litere_mari+ecx]
            mov [max], eax
            nu_e_mai_mare:
            loop repeta2
            
        
        mov ecx, 26
        repeta3:
            push ecx;cand ecx=0 nu mai intra in loop,deci ca sa pop verifica si pt litera A
            mov eax,[max]
            cmp eax, [litere_mari+ecx]
            jne nu_e_egal
            
            ;s-a gasit deci trebuie sa afisez
            push dword [litere_mari+ecx]
            xor eax,eax
            mov al,'a'
            add eax,ecx
            push eax
            push dword formatafisare
            call [printf]
            add esp,4*3
            
            nu_e_egal:
            loop repeta3
            
            
             
            final:
             push    dword 0      ; push the parameter for exit onto the stack
             call    [exit]  
            
            
            
            
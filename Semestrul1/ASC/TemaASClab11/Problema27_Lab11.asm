; Se citeste un sir de numere din fisierul "numere.txt". Sa se creeze alte 2 siruri N - cu numere impare, P - numere pare si sa se afiseze in consola.


bits 32
global start


extern exit, printf, fscanf, fopen, fclose, system
import exit msvcrt.dll
import fscanf msvcrt.dll
import printf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import system msvcrt.dll

%include "nr_cif.asm"
%include "reversed_transformare.asm"

segment data use32 public data
    filename db "numere.txt", 0
    descriptor dd 0
    open_type db "r", 0
    format_input db "%d", 0
    format_output_imp db "Sirul de numere impare: %s ", 0
    format_output_pare db "Sirul de numere pare: %s", 0
    format_output db "%s ", 0
    lungime dd 0 
    numar dd 0
    N times 20 resd 0 ; sirul cu numere impare
    P times 20 resd 0 ; sirul cu numere pare
    i dd 0
    j dd 0
    endline db 10, 0
    numar_cifre db 0
segment code use32 public code
start:
    push dword open_type
    push dword filename
    call [fopen]
    add esp, 4 * 2
    mov [descriptor], eax
    cmp eax, 0
    je final
    
    ; citire numere
     citeste:

        push numar
        push format_input
        push dword [descriptor]
        call [fscanf]
        add esp, 4*3
        
        cmp eax, 1
        jne sari
        push eax
                
        mov eax, [numar] ; numarul curent din sir
        push eax
        call nr_cif ;rezultat in ecx
        
        mov [numar_cifre], ecx
        pop eax
        
        
        test eax, 1
        push eax
        jz par
            ;aici e impar
            mov edi, N ; sirul de numere impare
            mov eax, 0
            mov eax, [numar]
            mov edx, [i]
            inc edx
            mov [i], edx
            jmp nu_e_par
        par:
            ;aici e par
            mov edi, P
            mov eax, 0
            mov eax, [numar]
            mov edx, [j]
            mov [N + edx], eax
            inc edx
            mov [j], edx
        nu_e_par:
        pop eax
        cmp eax, 1
     jnz citeste
    sari:
    push dword N
    push dword format_output_imp
    call [printf]
    add esp, 4 * 2
    
    push dword endline
    push dword format_output
    call [printf]
    add esp, 4 * 2
    
    push dword P
    push dword format_output_pare
    call [printf]
    add esp,4 * 2
      
    final: ; close the file
    push dword [descriptor]
    
    call [fclose]
    add esp, 4

    push 0
    call [exit]

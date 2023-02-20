bits 32

global nr_cif
;global start      

;extern exit
;extern printf               
;import exit msvcrt.dll    
;import printf msvcrt.dll

;segment data use32 public data
    ;numar dd 254
    ;format db "%d", 0
 
;segment code use32 public code
    nr_cif:
        ;Calculeaza numarul de cifre a unui numar introdus ca parametru
        mov eax, [esp + 4] ; numarul 
        ;esp - adresa de revenire a functiei
        mov bl, 10
        mov ecx, 0
        
    repeta4:
        push eax
        pop ax
        pop dx
        
        div bl ; ah = eax % 10 / al = eax / 10 
        
        mov edx, 0
        mov dl, al
        
        mov eax, 0
        mov eax, edx
        inc ecx      ; contor de numere
        cmp dl, 0
        je atat
     jmp repeta4
        
        atat:
     ret
     
      ;start:
         
         ;mov eax, 0
         ;push dword [numar]
         ;call nr_cif
         ;add esp, 4 * 1
            
         ;push dword ecx
         ;push dword format
         ;call [printf]
         ;add esp ,4 * 2
        
    
         ; exit(0)
         ;push    dword 0      ; push the parameter for exit onto the stack
         ;call    [exit]       ; call exit to terminate the program

        
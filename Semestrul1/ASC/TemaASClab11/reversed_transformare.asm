bits 32
;global start      

;extern exit
;extern printf               
;import exit msvcrt.dll    
;import printf msvcrt.dll

;segment data use32 public data
    ;numar dd 2559
    ;format db "%s", 0
    ;sir times 10 db 0
    ;nr_cif db 4
    
;segment code use32 public code
    global reversed_transformare  

    reversed_transformare:
    ; esp-adresa de revenire
    ; esp+4-adresa numarului de transformat
    ; esp+8-adresa numarului transformat in sir
    mov bl, 10
    mov ecx, dword[esp+12]; numarul de cif
    mov edi, dword[esp+8] ;sir
    mov eax, dword[esp+4] ;eax=numarul
    
    cld
        
        repeta3:
            div bl ; al = ax / 10, ah = ax % 10
            mov edx, 0
            mov dl,al       ; dl = al ; dl = catul impartirii
            mov al, ah      ; al = restul impartirii
            add al, "0"     ; al = al + 30
            mov [edi + ecx - 1], al
            mov eax, 0      ; eax = 0
            mov eax, edx    ; eax = catul
            dec ecx         ; numarul de cifre
            cmp eax, 0      ; daca nu mai avem cifre iesi
            je afara
            
        jmp repeta3
    afara:
    ;rezultat in eax
    ret

     ;start:
         ;push dword [nr_cif]
         ;push dword sir
         ;push dword [numar]
         ;call reversed_transformare
         ;add esp, 4 * 3
            
         ;push dword eax
         ;push dword format
         ;call [printf]
         ;add esp ,4*2
        
    
         ; exit(0)
         ;push    dword 0      ; push the parameter for exit onto the stack
         ;call    [exit]       ; call exit to terminate the program

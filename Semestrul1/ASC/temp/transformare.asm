bits 32

;global start      



;extern exit,printf               
;import exit msvcrt.dll    
;import printf msvcrt.dll
;segment data use32 public data
    ;sir db '200', 0
    ;len equ $-sir
    ;format db "%d", 0
segment code use32 public code
    global transformare
    transformare:
    ; esp-adresa de revenire
    ; esp+4-adresa sir
    ; esp+8-valoare len
        
        mov ecx, [esp+8] ; ecx = len
        dec ecx          ; ecx = ecx - 1 ; numarul de cifre
        mov ebx, 1       ; ebx = 1 ; putere a lui 10
        mov edx, 0       ; edx = 0 ; rezultatul final
        mov esi, [esp+4] ; esi = adresa sir
        repeta:
            mov eax, 0   ; eax = 0
            mov al, [esi+ecx-1] ; al = sir + len - 1
            sub al, '0'  ; al = al - 30 = al - '0'
            mul bl       ; ax = al * bl
            add edx, eax ; edx = edx + eax ;
            
            mov al, bl   ; al = bl ; al = 1
            mov bl, 10   ; bl = 10
            mul bl       ; ax = al * bl = 1 * 10 = 10
            mov ebx,eax  ; ebx = eax ; se salveaza puterea lui 10
        
        loop repeta
        ;edx = rezultat final
        ret
        
     ;start:
    
         ;push dword len ;esp + 4 * 2
         ;push dword sir ;esp + 4 * 1
         ;call transformare; esp + 0 ; adresa de revenire
         ;add esp, 4*2
         
         ; edx = rezultatul functiei
         
         ;push dword edx 
         ;push dword format
         ;call [printf]
         ;add esp ,4*2
        
        
        ;push    dword 0      
        ;call    [exit]       

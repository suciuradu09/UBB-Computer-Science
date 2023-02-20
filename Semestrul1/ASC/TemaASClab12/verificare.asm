bits 32

; informam asamblorul ca dorim ca functia _afisare_sir sa fie disponibila altor unitati de compilare
global _paritate
extern _printf
; linkeditorul poate folosi segmentul public de date si pentru date din afara
segment data public data use32

; codul scris in asamblare este dispus intr-un segment public, posibil a fi partajat cu alt cod extern
segment code public code use32

; int paritate(int num)

_paritate:
    ; creare cadru de stiva pentru programul apelat
    push ebp
    mov ebp, esp
    mov eax, 0
    mov edx, [ebp + 8]
    ; obtinem argumentele transmise pe stiva functiei sumaNumere
    ; la locatia [ebp+4] se afla adresa de return (valoarea din EIP la momentul apelului)
    ; la locatia [ebp] se afla valoarea ebp pentru apelant
    test edx, 1
    jz par
       ;impar
       mov eax, 0
        jmp sari
    par:
        ;par
        mov eax, 1
    sari:
    ; refacem cadrul de stiva pentru programul apelant
    mov esp, ebp
    pop ebp

    ret
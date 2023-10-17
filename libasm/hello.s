        global  _main
        extern  _printf

        section         .text
_main:
;       read from stdin
        mov     rax, 0x02000003 ; sys_read
        xor     rdi, rdi ; fd == stdin
        mov     rsi, buf ; buf as buf addr
        mov     rdx, 80  ; set buf size
        syscall

;       count number & print result
        sub     rsi, 1
        mov     rbx, -1        ; init rbx to store cnt ... can it be initialized as minus 1?
        xor     dl, dl        ; set rdx to 0
count:
        inc     rsi
        inc     rbx
        cmp     byte [rsi], dl  ; compare if it is null byte
        jne     count
        mov     rdi, format
        mov     rsi, rbx
        call    _printf         ; takes rdi, rsi as parameter in order

;       exit
        mov     rax, 0x02000001 ; sys_exit
        xor     rdi, rdi ; exitcode = 0
        syscall

        section         .data
format: db      "%20ld", 10, 0

        section         .bss
buf:   resb      80
        global    _main

        section         .text
_main:
        mov     rax, 0x02000003 ; sys_read
        xor     rdi, rdi ; fd == stdin
        mov     rsi, buf ; buf as buf addr
        mov     rdx, 80  ; set buf size
        syscall

        mov     rax, 0x02000004  ; sys_write
        mov     rdi, 1  ; fd == stdout
        mov     rdx, 80 ; buffer size ... why should i set this again?
        syscall

        mov     rax, 0x02000001 ; sys_exit
        xor     rdi, rdi ; exitcode = 0
        syscall

        section         .bss
buf:   resb      80
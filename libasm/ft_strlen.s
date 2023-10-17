        global    _main

        section   .text
_main:  
		mov		rsi, message - 1		; [message]? message?
		mov		rdi, res				; 출력할 결과물
		mov		r8, -1					; strlen 초기값
count_str:
		inc		rsi
		inc		r8
		cmp		byte [rsi], 0
		jne		count_str
;to_str:
;		;		strlen을 string으로 바꿔야...!
;		cmp		r8, 0
;		jne		to_str
		mov		rdi, r8
		mov       rax, 0x02000004         ; system call for write
        mov       rdi, 1                  ; file handle 1 is stdout
        mov       rsi, res            ; address of string to output
        mov       rdx, 2                ; res의 크기... 어떻게 세야할까?
        syscall                           ; invoke operating system to do the write
        mov       rax, 0x02000001         ; system call for exit
        xor       rdi, rdi                ; exit code 0
        syscall                           ; invoke operating system to exit


        section   .data
message:  db        "012345678901234567890123456789012", 0      ; note the newline at the end \
                                            (what is 10 at the end? : newline) \
                                            when you use backquotes, you can use excape sequences
        section     .bss
strlen: resb    8   ; 0으로 초기화 될까?
res:	resb	8	; 크기는 고정인가...?
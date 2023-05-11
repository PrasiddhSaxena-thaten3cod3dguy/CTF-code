
**Name** : stack_heap

**Category** : Pwn

**Difficulty** : Easy

**Flag** : HACKERSHALA{wh3n_4_d00r_cl0535_4n07h3r_0n3_0p3n5}

**Challenge description** : 
No way home T_T

**Background**: 

+ Open the binary in IDA.
+ Analyse the binary.
+ Find the format string bug.
+ Leak libc with fmt bug -> overwrite strchr_nul in libc GOT -> win.

**Hint**
1. `printf(arg)`

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
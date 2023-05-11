
**Name** : OOB

**Category** : Pwn

**Difficulty** : Medium

**Flag** : HACKERSHALA{7yp3_c0nfu510n_x0r_4n_00b}

**Challenge description** : 
scanf isnt that bad

**Background**: 

+ Open the binary in IDA.
+ Analyse the binary.
+ Send your ROP chain in first input it is stored in bss.
+ Find the OOB in getInt function.
+ Binary has canary enabled so at canary offset input `+` to bypass overwriting cookie and overwrite rip with pop rsp and stack pivot to bss where you stored the actual rop.

**Hint**
1. None

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
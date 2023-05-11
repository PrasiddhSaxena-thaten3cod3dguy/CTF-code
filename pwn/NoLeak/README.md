
**Name** : NoLeak

**Category** : Pwn

**Difficulty** : Hard

**Flag** : HACKERSHALA{f50p_3xpl0175_4r3_cr4zy}

**Challenge description** : 
Is it Actually a Leak less heap exploit? 

**Background**: 

+ Open the binary in IDA.
+ Analyse the binary.
+ Find the UAF and Double free bug in delete function.
+ You can also get a Heap overflow  and Write After Free primitive in Edit function.
+ Use partial overwrite 4bit bruteforce & Overwrite stdout to get libc leak.
+ Overwrite __free_hook -> system -> shell. 

**Hint**
2. 0xfbad1800

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
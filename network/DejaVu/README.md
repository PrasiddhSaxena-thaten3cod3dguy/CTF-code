**Name** : DejaVu

**Category** : Network

**Difficulty** : Medium

**Flag** : HACKERSHALA{r4c1ng_4g41nst_t1m3_e47ff2fc}

**Challenge description** : 
Have you ever felt dejavu?

**Background**: 

+ Foothold on the system is achieved through CVE-2021-22204 - a RCE in exiftool utility.
+ Horizontal escalation is done by decompiling a binary and exploiting an OS command injection in the custom binary.
+ Finally a race condition vulnerability is exploited in a bash shell script to get root on the box.

**Hint**
1. Figure out how the backend might be working.
2. To break things, you must know how it is built (its my favorite line tho :))
3. You must win the race to get the flag :)

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
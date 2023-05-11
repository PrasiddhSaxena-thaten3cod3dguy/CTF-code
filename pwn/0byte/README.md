
**Name** : 0byte

**Category** : Pwn

**Difficulty** : Medium

**Flag** : HACKERSHALA{fr0m_null_by73_70_5h3ll_w3_pr0_up_9876512}

**Challenge description** : 
0 bytes of Power. 

**Background**: 

+ Open the binary in IDA.
+ Analyse the binary.
+ Find the null byte overflow bug in get_input function
+ Heap Feng Shui and Shell

**Hint**
1. `buf[i]='\0';`

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
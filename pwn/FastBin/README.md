
**Name** : FastBin

**Category** : Pwn

**Difficulty** : Hard

**Flag** : HACKEHACKERSHALA{y0u_c4n_7074lly_d0_7h15_89723}

**Challenge description** : 
What if a link is converted to a circle ?

**Background**: 

+ Open the binary in IDA.
+ Analyse the binary.
+ Find the obvious UAF bug.
+ Use the UAF and Double free on fastbins.
+ Create a overlapping chunk and change size of one heap chunk to 0xa1 so that when freed it ends up in unsorted bin.
+ You cannot overwrite __malloc_hook or anything as you can't get off easily having a fd pointed to the libc region. 
+ Use unsorted bin attack along with House Of Orange for shell.

**Hint**
1. free(ptr) = NULL is a good practise.

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements

**Name** : Power

**Category** : Pwn

**Difficulty** : Medium

**Flag** : HACKERSHALA{https://securitylab.github.com/research/last-orders-at-the-house-of-force/}

**Challenge description** : 
Power of Heap ?

**Background**: 

+ Open the binary in IDA.
+ Analyse the binary.
+ Find the Heap Overflow in Edit function. You cna use it only once.
+ You can create a large size chunk only once.
+ Use Unsorted bin to leak libc.
+ Use edit function to overwrite top_chunk.
+ Use a large allocation for House Of Force Primitive.
+ overwrite __malloc_hook to one_gadget and gain shell.

**Hint**
1. scanf("%s", heap_note[idx]);

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements

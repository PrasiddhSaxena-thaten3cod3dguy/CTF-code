**Name** : vocal-for-local!!

**Category** : Web

**Difficulty** : Easy

**Flag** : HACKING_BRAWL{Inclu510n_n1nj4!!!}

**Challenge description** : 
Use the same key to unlock different lock.txt.


**Background**: 
+ User is provided with a blog application.
+ The blog is fetched using a get parameter named `blog-id`.
+ This parameter fetches files from the machine and is therefore vulnerable to LFI.
+ To find the flag, user will request for `?blog-id=flag.txt`.
+ Flag will be fetched on the app.

**Hints**
1. flag.txt

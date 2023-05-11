**Name** : catch the ghost

**Category** : OSINT

**Difficulty** : Easy

**Flag** : HACKING_BRAWL{p45t3_and_f0rGet!}

**Challenge description** : 
A deadly ghost knows the secrets to all your problems. The secret is hidden in a place inaccessible to humans.


**Background**: 
+ User is given access to a web page with an input field.
+ On giving any input to the webpage, user will recieve a warning saying that:
    *No noob attempts. The secret is under my robot's protection at locker number - i4dSV*
+ Here, it hints that something is stored at robots.txt.
+ When user visits `/robots.txt`, they will find ghostbin password.
+ The locker number above is the ghostbin endpoint where flag is stored.
+ User will the visit [https://ghostbin.com/i4dSV/Hackingbrawl](https://ghostbin.com/i4dSV/Hackingbrawl) to get the flag.

**Hints**
+ Sufficient hints are present. 
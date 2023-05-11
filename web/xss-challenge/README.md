**Name** : F1lt3r_coffee!

**Category** : Web

**Difficulty** : Easy

**Flag** : HACKING_BRAWL{XSS_EV3Rywh3re}

**Challenge description** : 
You do love cookies, don't you? 
Well, we have opened our cookie shop for the ctf players. Search for you 
favourite cookie and enjoy with our home brewed filter coffee. 


**Background**: 

+ User gets access to webpage with a search functionality.
+ All the search parameter gets refelcted in the webpage itself but `script` is filtered out using :
  
  `$pattern = '/script/i';`

   `$payload = preg_replace($pattern, '', $payload);`
+ User can get a hint of this function by clicking on **Get free filter coffee!**
+ Flag is displayed only when user is succesfully able to pass the following search query :

`<script>alert(document.cookie)</script>`

+ This can be achieved by putting another **script** string between the script string like this :

`<scrscriptipt>alert(document.cookie)</scscriptript>`

+ Internal script will be filtered out and left-right substring will combine again to form **script**
**Name** : crack-true-crack

**Category** : Web

**Difficulty** : Easy

**Flag** : HACKING_BRAWL{y0u_k33n_obs3rv3r}

**Challenge description** : 
Tell me the secret and get your flag. I answer all your queries only if you know how to ask. 


**Background**: 
+ User is provided with a sample webpage containing an input field.
+ User needs to enter the password and get the flag.
+ Whenever an input is provided, request is made to `/index.php?password=<password>&view-source=false`
+ On change view-source to `true`, code snippet will be shown on the web page :
  
        if(md5(password) == '9fd8301ac24fb88e65d9d7cd1dd1b1ec')
          {

              showFlag();}

          else

          {
              hideFlag(); 
        };
+ This gives a hint that whatever input is given by the user, it is converted into md5 hash and then compared to password in the backend.

+ To find the exact password, user will need rainbow tables such as [this](https://crackstation.net/).
+ User will find that given passsword is `butterfly` and then get the flag.

**Hint** 
1. Can you crack the station?
2. Rainbows are beautiful.
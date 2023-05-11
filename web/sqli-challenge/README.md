**Name** : Err0rl3ss 1nject0r!

**Category** : Web

**Difficulty** : Easy

**Flag** : HACKING_BRAWL{SQLi_with0ut_3rr0r}

**Challenge description** : 
Injections here, injections there but no error to find anywhere. That's all you need to get going. Login and get the flag Mr. hacker. 


**Background**: 

+ User get access to a web application with login functionality.
+ The username field is injectable with even the simplest of sqli payloads like :

    + `' or true #`
    +  ` 'or 1=1#`
+ User needs to use any such payload which evaluates to true.
+ Once user has injected the payload, they will be logged in and get access to the flag.

**Deployment**
+ Just run `docker-compose up`  
+ By default, web app will run on port *2408* and mysql on port *9906*.
+ Changes can be made as per requirment in the *docker-compose.yml* file
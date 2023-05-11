**Name** : Manipulator_the_injector!

**Category** : Web

**Difficulty** : Easy

**Flag** : HACKING_BRAWL{SQLi_&&_manipul4t10n}


**Challenge description** : 
I know that you can break through login verifications but can you break through my filters? 


**Background**: 

+ User get access to a web application with login functionality.
+ The username field is injectable with even the simplest of sqli payloads like :

    + `' or true #`
    +  ` 'or 1=1#`
+ But all such payloads which include `true`, `1=1` can't pass through the backend filter.
+ Whenever a request is submitted, an ajax call is made to `check.php` to verify the input data.
+ `check.php` returns *false* for all trivial payload injection.
+ There are several methods to solve this challenge :
  + Make a post request directly to `verify.php` with the relavant parameters.
  + Use well crafted payloads.
  
+ ### Preferred solution :
  + Turn on burp, insert payload-> intercept the request to check.php-> intercept response to request.
  + Change *false* to *true* in the response.
  + payload will be executed
      
**Hint**
+ Your request depends on my response.
+ Why is ajax such a pain?
  
**Deployment**
+ Just run `docker-compose up`  
+ By default, web app will run on port *2408* and mysql on port *9906*.
+ Changes can be made as per requirment in the *docker-compose.yml* file
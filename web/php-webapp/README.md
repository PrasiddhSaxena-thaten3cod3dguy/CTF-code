**Name** : R0ck_The_C00k13.txt

**Category** : Web

**Difficulty** : Easy

**Flag** : HACKING_BRAWL{Bru73_C00k13}

**Challenge description** : 
We heard you don't need username and passwords to login. Go ahead and show us your skills. Our user is still living in the 90s and uses a weak password. 

Health tip - Stay **hydra**ted.

**Background**: 

+ Once machine is deployed, user will get access to a login page with username and password fiels.
+ When user tries to login using any credentials, the username is leaked in the response cookie.
+ Once our user has the username, he will need to brute-force the login using hydra and rockyou.txt. 
+ Sufficient hint is provided in the challenge description to indicate the use of hydra and rockyou.txt.
+ Hydra script :
  
   `hydra -s <port-num> -l <username> -P ./path/to/rockyou.txt <server-ip> http-post-form "/index.php:username=<username>&password=^PASS^:Wrong password" -V -I`

+ Once the password is cracked, user will login and get the flag.
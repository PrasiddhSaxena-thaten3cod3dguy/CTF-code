**Name** : IDOR lab 2

**Category** : Web

**Difficulty** : Medium

**Flag** : HACKERSHALA{1D0Rs_1n_API_vhnrdfvijg}

**Challenge description** : 
There are more secrets than you think.

**Background**: 

+ While registering a user, the application reveals API secret.
+ You can also find the secret from static JS file.
+ You need to do some API fuzzing to get an API endpoint.
+ Then a classic IDOR to finally get the flag.
+ Find the flag at - `/api/v1/users/527e3b6bf06f3d3358905af67c588b1ba621a8599b6010e1a0556632b3c5a2ee/0/flag`

**Hint**
1. You can not see everything through the same eye.

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
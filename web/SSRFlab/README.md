**Name** : SSRFlab

**Category** : Web

**Difficulty** : Medium

**Flag** : HACKERSHALA{p3rf0rm1ng_1nt3rn4l_p0rt_sc4n_thr0ugh_SSRF_chgdrbyturg}

**Challenge description** : 
A simple application. Atleast this is what is looks from outside, isn't it ?

**Background**: 

+ User can add a URL to create a profile picture.
+ This can be leveraged to perform an internal port scan through SSRF.
+ However almost all of the filter bypassing payloads are filtered here.
+ Again, blacklist based filters can be bypassed easily.
+ Port 1337 is open internally.
+ Then user need to do content-discovery to find an endpoint `/flag` which reveals the flag.
+ Payload - `http://lOcAlHoSt:1337/flag`

**Hint**
1. Check the application carefully. See what is permitted and what is not.

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
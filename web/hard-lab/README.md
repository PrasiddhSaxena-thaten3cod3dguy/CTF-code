**Name** : DBS - Hard lab

**Category** : Web

**Difficulty** : Hard

**Flag** : HACKERSHALA{ssrf_t0_sql1_t0_4rb1tr4ry_f1l3_r34d5_7cc9ebb9}

**Challenge description** : 
Are you a DBS fan ?!?

**Background**: 

+ The challenge involves exploiting 3 different vulnerabilities.
+ It begins with a SSRF that reveals an internal web service.
+ The internal website is vulnerable to SQLi which reveals admin credentials on the main app.
+ After logging into the main application, an arbitrary file read vulnerability can be found.
+ Using this, you can read the flag in the root fs.
+ All of the 3 vulnerabilites are protected (isnt it? :)) through some simple filters which can be bypassed.

**Hint**
1. Vulnerabilities everywhere !!!!

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
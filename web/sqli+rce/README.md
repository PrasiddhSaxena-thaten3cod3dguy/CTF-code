**Name** : Simple blogsite 2

**Category** : Web

**Difficulty** : Medium

**Flag** : HACKERSHALA{sql1_t0_rc3_gvuthnnfiuhnitru}

**Challenge description** : 
Simple website, is not it ?

**Background**: 

+ The challenge starts with a second order SQLi
+ Inject the payload while signing up.
+ Trigger the payload after logging in.
+ Find admin password using sqli.
+ After logging in as admin, it is a simple RCE to get flag.

**Hint**
1. It simple. Dont think too hard.

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
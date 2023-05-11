**Name** : Insecure validation lab

**Category** : Web

**Difficulty** : Medium

**Flag** : HACKERSHALA{4dm1n_t4k30v3r_us1ng_1ns3cur3_v4l1d4t10n}

**Challenge description** : 
Can you figure out what is wrong with my web app ?

**Background**: 

+ There is a validation issue after decoding JWT token which leads access to sensitive endpoint `/admin`.
+ The application is not checking for any trailing spaces after a username. (There is a check for spaces at front however).
+ So the application parses "admin" and "admin  " as the same. Notice the space after the second admin.
+ So a user can create a user with name "admin " and takeover admin account.

**Hint**
1. You got to learn trickery.

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
**Name** : Capsule Corp

**Category** : Web

**Difficulty** : Medium

**Flag** : HACKERSHALA{3xpl01t1ng_1D0Rs_lyk_4_pr0_vbdrhgudrfvuderjbyhgvredgvuijb}

**Challenge description** : 
Capsule Corp wants you to pentest their site. 

**Background**: 

+ You can create a user in the web application.
+ Then you exploit a weak JWT secret to takeover admin account through IDOR.
+ Then you exploit another IDOR vulnerability to access unauthorized static files.

**Hint**
1. Some secrets are meant to be secret ;)

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
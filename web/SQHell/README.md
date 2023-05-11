**Name** : SQHell.

**Category** : Web

**Difficulty** : Medium

**Flag** : HACKERSHALA{SQL_1nj3ct10n_f0r_da_w1n}

**Challenge description** : 
Let me show you my secure web application. Oh, did I say "secure" ? Well I dont know.

**Background**: 

+ Second order SQL injection on the application.
+ Inject the SQLi payload in the username field on the signup page.
+ Trigger it after logging into the application.
+ Blacklist based filter is in black ground.
+ Retrive flag from `flag` column in `flag` table in the same db. Payload - `admin' uNiOn SelEcT flag FrOm flag -- -`

**Hint**
1. The name of the challenge rhymes with something ?!?

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
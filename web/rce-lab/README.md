**Name** : Domain2IP

**Category** : Web

**Difficulty** : Medium

**Flag** : HACKERSHALA{bl4ckl1sts_c4n_b3_byp4$$3d_34s1ly_fueferhgyr8t}

**Challenge description** : 
This is an application that gives the IP of the corresponding domain name.

**Background**: 

+ The backend is running dig on the user input.
+ Most of the characters are filtered except `.`, `|` and `'`.
+ Some commands are also blacklisted like `cat`, `ls`.
+ Get the flag by - `google.com| c''a''t f''l''a''g.txt`

**Hint**
1. Check what things you can use.

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
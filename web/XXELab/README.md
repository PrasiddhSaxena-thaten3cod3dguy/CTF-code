**Name** : TODO-App

**Category** : Web

**Difficulty** : Medium

**Flag** : HACKERSHALA{xxe_t0_p0rt_scann1ng_t0_fuzz1ng_lyk_4_pr0}

**Challenge description** : 
I have built a TODO app so that I do not forget what I have to do. Can you make this simple app to do things it was not intended to do ?

**Background**: 

+ A XXE injection is present while adding a TODO.
+ Using XXE to internally scan the system to find another application running on port 1337.
+ Again using XXE, fuzzing the internal web application will reveal a path `/contents/flag`
+ Finally you will get the flag.

**Hint**
1. Just when you think you found everything about the application, you might need to rethink it.

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
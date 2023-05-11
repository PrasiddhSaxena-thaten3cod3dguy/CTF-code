**Name** : Blogsite

**Category** : Web

**Difficulty** : Medium

**Flag** : HACKERSHALA{sst1_1s_c00l_1snt_1t?}

**Challenge description** : 
I have created a simple blog application that seems secure, isn't it ?

**Background**: 

+ A simple application having SSTI.
+ There is a blacklist in place that blocks most of keywords relevant to SSTI.
+ However you can read the flag as it is in the web root.
+ Payload - `{{"".__class__.__base__.__subclasses__()[92].__subclasses__()[0].__subclasses__()[0]("flag.txt").read()}}`
+ Here the payload is using the python IObase class to read a file, `flag.txt`.

**Hint**
1. What you do when you see yourself on the mirror?

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
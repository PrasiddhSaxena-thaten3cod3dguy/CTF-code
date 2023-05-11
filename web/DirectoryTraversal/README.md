**Name** : Directory Traversal.

**Category** : Web

**Difficulty** : Medium

**Flag** : HACKERSHALA{D0tD0tSlash_D0tD0tPwn}

**Challenge description** : 
Turtle Hermit Academy chooses you to test their website for security vulnerabilities. Will you be able to show your elite skills ? 

**Background**: 

+ Fuzzing on `/brochure` reveals a parameter `path`.
+ Directory fuzzing reveals `/static/uploads`.
+ The parameter `path` only accepts values starting with `/static/uploads`.
+ The parameter `path` is vulnerable to Directory traversal.
+ POST request to `/brochure` with `path` parameter having value `/static/uploads/../../../../../../opt/flag.txt` will reveal the flag.

**Hint**
1. You do not always GET what you want.
2. To get the flag, you must **opt** for it.

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
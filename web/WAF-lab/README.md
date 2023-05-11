**Name** : WAF Bypass

**Category** : Web

**Difficulty** : Medium

**Flag** : HACKERSHALA{Byp4$$1nG_W4Fs_c4n_b3_sup3r_34sy_31337}

**Challenge description** : 
An application where you can find subdomains of a domain.

**Background**: 

+ The application is using `subfinder` tool to find subdomains.
+ The only malicious character allowed is `;`.
+ The application expects `cat` keyword after `;`, but `cat` along with some other keywords are blacklisted.
+ You can however bypass this filter.
+ Get the flag - `nehal.rocks; ccatat flflag.txtag.txt`

**Hint**
1. See what characters are allowed.
2. Find the logic of how malicious characters might be handled in the backend.

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
**Name** : Whoisapp

**Category** : Network

**Difficulty** : Medium

**Flag** : HACKERSHALA{qu1t3_4_j0urn3y_0ec4b21a}

**Challenge description** : 
A simple application to fetch WHOIS data

**Background**: 

+ User need to exploit an RCE on webite at port 80.
+ Then user need to analyse an iso file that reveals a system-user password.
+ The system-user has a sudo privilege.
+ You get root by hijacking a python module.

**Hint**
1. There might be filters in the website :)

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
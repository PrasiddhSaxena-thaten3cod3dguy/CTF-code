**Name** : Hardcoded issue lab

**Category** : Web

**Difficulty** : Medium

**Flag** : HACKERSHALA{h4rdc0d3d_s3cr3t5_4r3_d4ng3r0u5_gvrdhguyhrtbgiofhnsdefuikgjedrbuyg}

**Challenge description** : 
What happens when a novice developer hardcodes his secrets somewhere?

**Background**: 

+ User first need to exploit a LFI on `/image` endpoint.
+ He can read the source code at `/image=static/img/../../app.py`.
+ Then he can find the JWT hardcoded secret from `.env` file.
+ After that he will forge a malicious JWT token to get admin rights.
+ Then he exploits a command injection vuln.
+ However there is a filter that blacklists almost all the malicious characters and some linux commands.
+ Get the flag at `/dashboard?cmd=c''at fl''ag_vbfduergsfffvnberudfgvniujngbesdr/f''lag.txt`
.

**Hint**
1. Guess what technology the backend is using.
2. If you were a dev, where will you keep your secrets to prevent hardcoded issues ?

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements

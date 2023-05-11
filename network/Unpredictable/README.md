**Name** : Unpredictable

**Category** : Network

**Difficulty** : Medium

**Flag** : HACKERSHALA{Y0u_d3s3rv3_4_fl4g_a39cd32}

**Challenge description** : 
Allmight always says, "Go Beyond Plus Ultra"

**Background**: 

+ First the user needs to bypass an IP based filter to access website.
+ Then a weak JWT secret is forged to get admin role which is 0.
+ But the user can not directly forge a cookie with role id 0.
+ The users needs to exploit an integer overflow vulnerability to forge a cookie with role id 0.
+ After accessing admin panel, the user finds an LFI.
+ Using the LFI, the needs to analyse the source code.
+ The source code will reveal that the website is vulnerable to SSTI at a secret endpoint.
+ The SSTI will give the shell as www-data.
+ The user then needs to exploit PwnKit CVE 2021-4034 to get root on the box.

**Hint**
1. There can more than one way to solve a particular problem.
2. Use what you have to find what you dont know yet.
3. Sometimes things are pretty obvious.

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
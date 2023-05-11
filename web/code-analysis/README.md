**Name** : All about analysis.

**Category** : Web

**Difficulty** : Easy

**Flag** : HACKING_BRAWL{C0D3_AN4LY515_FTW}

**Challenge description** : 
Can you login with a valid username and password?

Just don't come asking for hints, you are provided with more than what you need.

**Background**: 

+ User is given access to a login page.
+ User password and username is validated by the `index.js` file.
+ Upon close analysis and little bit of javascript knowledge, user can find out that username and password is hard-coded in base64.
+ User will then decode username and password.
+ username : *0x01_student*, password : *verysecureP4ssw0rd*

**Hint**
1. Not needed

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
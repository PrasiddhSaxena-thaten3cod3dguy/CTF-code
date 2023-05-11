**Name** : dGFtcGVyIHRoZSBoYXNo

**Category** : Web

**Difficulty** : Easy

**Flag** : HACKING_BRAWL{base64_why??}

**Challenge description** : 
Do you have sufficient funds to buy the flag of destiny?
Can you bargain? 

**Background**: 

+ User is given access to a web application where they are supposed buy flag by clicking on the buy button.
+ The cost of flag is $10 but user's wallet balance is $0.
+ The cost of flag and balance of user is passed as base64 encoded json string `eyJiYWxhbmNlIjowLCJjb3N0IjoxMH0=`.
+ This decodes to `{"balance":0,"cost":10}`
+ To be able to buy the flag, user needs to change the values such that balance is greater than the cost. 
+ The changed JSON will then be encoded in a base64 string and will replace the original base64 string.
+ One valid base64 string is :`eyJiYWxhbmNlIjoxMCwiY29zdCI6MTB9`.
+ Upon succesful attempt, user will get the flag.

**Hint**
1. 64th basement.

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
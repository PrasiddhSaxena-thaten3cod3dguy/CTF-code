**Name** : Mr Extr4ct0r

**Category** : Network

**Difficulty** : Easy

**Flag** : HACKINGBRAWL{INS3CURE_FTP!}

**Challenge description** : A hacker intercepted the traffic from hackershala. There are some sensitve information being transferred on the network. Can you help us figure out the leaked information?

**Background**: 

+ A pcap file containing tcpdump of ftp traffic and some random traffic is given to the user.

+ The user needs to open it with wireshark and apply the filter `ftp-data`.

+ In the filtered results, user will right click on data packet which shows `flag.png` and then `follow TCP stream`.
+ The user will then export the TCP stream as `raw` and save it as `any-name.png`.
+ The exported png file will contain the flag.

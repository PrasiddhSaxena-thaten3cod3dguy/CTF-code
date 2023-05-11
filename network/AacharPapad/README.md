**Name** : AacharPapad

**Category** : Network

**Difficulty** : Medium

**Flag** : HACKERSHALA{4ll_p1ckl3s_4r3_n0t_900d_88cbef}

**Challenge description** : 
Get the world class pickles from Madhvi Bhabhi.

**Background**: 

+ Foothold on the system is achieved through an RCE using python module pickle used for serialisation-deserialisation.
+ Then escalate horizontally to a system user by reversing a crypto algorithm.
+ Then comes the most hard part of the box - Privilege escalation.
+ This part may be a little tough due to a little rabbit hole and a pretty unique style of exploitation.
+ User needs to exploit the SUID capability of capsh utility to get root on the box.

**Hint**
1. Some pickle are just too terrible.
2. When GTFObins fail, linux manpage for your rescue.

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
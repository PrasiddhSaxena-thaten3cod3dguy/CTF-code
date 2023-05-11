**Name** : Adm1n_th3_man1pul4t0r

**Category** : Web

**Difficulty** : Easy

**Flag** : HACKING_BRAWL{adm1n_pr1l1v1g3s_ftw}

**Challenge description** : 
Our admin is a great manipulator. Let's see if you can manipulate him and extract the flag. 


**Background**: 
+ User will be provided with a login page.
+ On making an invalid request, test credentias will be displayed to the user:
  >Use following credentials to login
  
    >username:t357_user

    >password:l0gm31n

+ Using these credentials, user will be logged in with *user-level privileges*.
+ This privilege is decided according to a cookie named *role*.
+ To gain admin privilege user will need to change the value of *role* to *admin*.
+ This can be done using [cookie editor](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/) or dev tools.
+ Once user has succesfully manipulated the cookie, they will be able to see the flag.
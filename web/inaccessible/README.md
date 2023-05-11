**Name** : Dash_7h3_b0ard!!

**Category** : Web

**Difficulty** : Easy

**Flag** : HACKING_BRAWL{ev3ry1_l0v3s_ki77y}

**Challenge description** : 
Do it when they believe that you can't. If the door is closed, break the walls. 


**Background**: 

+ User is provided with a login page without any credentials.
+ On entering any random credentials, user is directed to `/verify.php` page which says : 

    *Sorry you can't access the dashboard*
+ This hint is enough to indicate that user should directly visit the `/dashboard.php` page.
+ On visiting `/dashboard.php`, user is given an input where he can ask for the flag.
+ On typing anything in the input field and submitting the *ask* button, alert message will appear saying : *Kitty.txt isn't impressed. Try harder!!*
+ To find the flag, user needs to type *cat flag.txt* and click on *ask* button.
+ Enough hints are provided in the page header for this.

**Hints**
1. Can you access the inaccessible?
2. How will you read flag.txt?

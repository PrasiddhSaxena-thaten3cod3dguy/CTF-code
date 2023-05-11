
**Name** : TERMinator dustBIN

**Category** : Web

**Difficulty** : Easy

**Flag** : HACKING_BRAWL{base64_why??}

**Challenge description** : 
 A hacker named *bu90* was recently accused of attacking our governmentHe was stolen some sensitive information and PASTEd it in his secret BIN.
 Can you help us find out which building was he targeting?

**Background**: 

+ The name of hacker bu90 points to a termbin [endpoint](https://termbin.com/bu90) where base64 string of image is stored.

+ User can extract image from the string using a [decoder](https://www.base64decode.net/base64-image-decoder.).

+ After downloading the image, user will run `exiftool <file.jpeg>` to extract GPS coordinates.
+ From there, user will visit [GPS locator](https://www.gps-coordinates.net/).
+ The name of building is *Rashtrapati-Bhawan* which is our flag. 

**Hint**
1. Something like pastebin.
2. Exif.


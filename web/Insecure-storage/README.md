**Name** : Insecure storage lab

**Category** : Web

**Difficulty** : Medium

**Flag** : HACKERSHALA{w34k_3ncrypt10n_t0_1ns3cur3_st0r4g3}

**Challenge description** : 
Lab demonstrating weak encryption of uploaded filenames lead to reading any file on the web file system.

**Background**: 

+ Only images are allowed to upload.
+ However file names are encrypted before they are stored in the website uploads dir.
+ The encryption being used here is a weak one involving an XOR operation.
+ Upload your own file to figure out the key for XOR.
+ Then create encrypted file name of `flag.txt` that will give you the flag.

**Hint**
1. Have you watched the eXORcist movie ?

**Deployment**
+ Just run execute.sh
+ Make necessary changes in execute.sh for custom requirements
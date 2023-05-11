import os

def find_ip(d):
    blacklist = ['"', ";", ":", "]", "}", "[", "{", "=", "+", ")", "(", "*", "&", "^", "%", "$", "#", "@", "!", "~", "`", ">", "<", ",", "\\", "/", "?", "ls", "cat", "flag.txt", "etc", "passwd", "home", "root"]
    for char in blacklist:
        if char in d:
            return "Hacker detected :)"
    return os.popen("dig +short " + d).read()
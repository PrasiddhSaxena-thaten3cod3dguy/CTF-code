import myutils

with open("/etc/passwd", "r") as rf:
    contents = rf.read().split("\n")
    myutils.printOdd(contents)
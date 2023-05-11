from os import popen

def find_subdomains(d):
    blacklist = ["~", "|", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "-", "`", "{", "}", "\\", '"', "'", ":", "/", "?", ">", ",", "<", "cat", "ls", "id", "etc", "passwd", "shadow", "flag.txt"]
    for word in blacklist:
        if word in d:
            d = d.replace(word, "")
    if d.startswith(";"):
        return ["No domain no flag."]
    if ";" in d:
        if not d.split(";")[1].strip().startswith("cat "):
            return ["Only cats allowed."]
    cmd = f"./tools/subfinder -silent -d {d}"
    return popen(cmd).read().split("\n")

if __name__ == "__main__":
    d = input("Enter the domain > ")
    subdomains = find_subdomains(d)
    for d in subdomains:
        print(d)
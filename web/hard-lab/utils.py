import requests
import random
import string

def get_image(url):
    r = requests.get(url)
    name = "static/img/" + "".join(random.choice(string.ascii_lowercase) for _ in range(10))
    with open(name, "wb") as wf:
        wf.write(r.content)
    return name

def check_url(url):
    mal = False
    if not url.startswith("http"):
        mal = True
    blacklist = ["127.0.0.1", "localhost", "LOCALHOST", "0.0.0.0", "[::]", "2130706433", "3232235521", "3232235777", "2852039166", "127.127.127.127", "127.0.1.3", "127.0.0.0", "0177.0.0.1", "o177.0.0.1", "0o177.0.0.1", "q177.0.0.1", "[0:0:0:0:0:ffff:127.0.0.1]", "127.", "@"]
    for word in blacklist:
        if word in url:
            mal = True
            break
    return mal

def check_field(field):
    blacklist = ["SELECT", "select", "UNION", "union", "FROM", "from", "WHERE", "where", "ORDER", "order", "NULL"]
    for word in blacklist:
        if word in field:
            return False
    return True

def check_filename(filename):
    mal = False
    if not filename.startswith("static/img/"):
        mal = True
    return mal
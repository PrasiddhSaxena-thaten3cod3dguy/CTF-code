import requests
import random
import string

def get_img_from_link(url):
    blacklist = ["localhost", "LOCALHOST", "[::]", "127.127.127.127", "0.0.0.0", "2130706433", "3232235521", "3232235777", "2852039166", "0177.0.0.1", "o177.0.0.1", "0o177.0.0.1", "q177.0.0.1", "@", "&"]
    if not url.startswith("http") or any(x in url for x in blacklist) or "127." in url:
        return "malicious"
    res = requests.get(url)
    filename = f"app/static/uploads/{''.join(random.choice(string.ascii_letters) for _ in range(10)) + '.png'}"
    with open(filename, "wb") as wf:
        wf.write(res.content)
    return filename

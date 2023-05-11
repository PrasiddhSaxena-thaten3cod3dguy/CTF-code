class Crypt:
    def __init__(self, ctext) -> None:
        self.ctext = ctext

    def encrypt(self):
        a = 0x13
        b = 0x37
        m = 0x1337
        enc = [(ord(c)^a + b) % m for c in self.ctext]
        return enc
    
    def save(self, f):
        enc = self.encrypt()
        with open(f, "w") as wf:
            wf.write(" ".join([str(x) for x in enc]))

    def decrypt(self, enc):
        # I am not able to reverse the logic, can you ?
        pass

if __name__ == "__main__":
    pwd = input("Enter your password >> ")
    filename = input("Enter filename to save >> ")
    ct = Crypt(pwd)
    ct.save(filename)
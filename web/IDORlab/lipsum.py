from faker import Faker
import random

files = []

while len(files) != 101:
    filename = f"{random.randint(1, 28)}-{random.randint(1, 12)}-{random.choice([19,20,21])}.txt"
    if filename not in files:
        files.append(filename)
        print(filename)
        with open(f"Application/static/reports_gvrb/{filename}", "w") as rf:
            fake = Faker()
            rf.write(fake.text())

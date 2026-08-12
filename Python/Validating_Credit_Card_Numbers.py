import re
for _ in range(int(input())):
    cd = input()
    if re.match(r'^[456]\d{15}$|^[456]\d{3}(-\d{4}){3}$', cd):
        cd2 = cd.replace('-', '')
        if not re.search(r'(\d)\1{3,}', cd2):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")

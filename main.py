check = ["root", "123456"]
m = 0

#check for user in file
def ufile(uName):
    global m
    global check
    file = open(r"C:\Users\Dude\PycharmProjects\pyUserLogin\users", "r").read().splitlines()
    for line in file:
        tmp = line.split("/")
        if uName == tmp[0]:
            check = tmp
            m = 1

#create a new user
def creat():
    global m
    uN = input("New User: ")
    uP = input("New Pass: ")
    kll(uN, uP)
    while len(uP) < 6:
        print("Pasword must be at least 6 len:")
        uP = input("New Pass: ")
        kll(uN, uP)
    ufile(uN)
    if m == 0:
        file = open(r"C:\Users\Dude\PycharmProjects\pyUserLogin\users", "a").write(f"\n{uN}/{uP}")
        print("Saved to file")
        m = 1
        exit()
    else:
        m = 0

#end this hell
def kll(uN, uP):
    if uN == "quit" or uP == "quit":
        exit()

while m == 0:
    uN = input("User: ").lower()
    uP = input("Pass: ")
    kll(uN, uP)
    ufile(uN)
    if uN != check[0]:
        print("User not found. Create a new one")
        while m == 0:
            creat()
            print("Already exists. Try another one")
    elif uN == check[0] and uP == check[1]:
        print(f"Hello, {check[0]}")
        m = 1
    else:
        print("Wrong pass. Try again.")
        m = 0

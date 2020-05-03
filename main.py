import berserk

with open("C:\\Users\\Petter\\Desktop\\PythonProjects\\lichess_token.txt") as f:
    token = f.read()

session = berserk.TokenSession(token)
client = berserk.Client(session)

# Gets your account data, e.g ["id"], ["username"]
#print(client.account.get())
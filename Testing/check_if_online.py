import random
import string
import webbrowser
from colorama import *

username = input('Enter your name: ')
def scramble():
    res = ''.join(random.choices(string.ascii_letters + string.digits, k = 5000))
    print(Fore.GREEN + 'CREATING RANDOM ROOM KEY CONSISTING OF 70 ASCII CHARS')

    print(Fore.BLUE + res)
    print("\n\n\n\n"+ Fore.GREEN +"generated random key ")

    webbrowser.get("firefox").open("http://104.197.154.60/chat?username={}&room={}".format(username,res))


init(convert=True)
friends = ["lisa","zoe","mark","Hello"]

print(""""
{}
{}
{}
{}
""".format(friends[0], friends[1], friends[2],friends[3]))
print(Fore.RED + 'This is list is hardcoded right now')

x = int(input("Who do you want to talk to?"))

choice = x - 1

scramble()

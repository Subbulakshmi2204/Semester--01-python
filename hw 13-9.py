"""
import random
def start():
    print("****Rolling dice****")
    comp_choice=random.randint(1,6)
    if comp_choice==1:
        print("1")
    elif comp_choice==2:
        print("2")
    elif comp_choice==3:
        print("3")
    elif comp_choice==4:
        print("4")
    elif comp_choice==5:
        print("5")
    else:
        print("6")
    play=input("Do you want to exit? Exit/No")
    if play=="No":
        start()
    else:
        print("Thanks for playing")
start()
import random
def start():
    print("Selecting a restaurant")
    comp_choice=random.randint(1,7)
    if comp_choice==1:
        print("Pind")
    elif comp_choice==2:
        print("Dominos pizza")
    elif comp_choice==3:
        print("Indian chappathis")
    elif comp_choice==4:
        print("A2B")
    elif comp_choice==5:
        print("Sangeetha")
    elif comp_choice==6:
        print("Animal kingdom")
    else:
        print("Komalas restaurant")
    pick=input("Pick a restaurant!Exit/Invalid input")
    if pick=="Invalid input":
        print("Invalid input")
    else:
        print("Exit")
start()"""
def validate(username):
    import string as s
    if username[0] not in s.ascii_letters:
        return "Must start with a letter."
    elif len(username) < 5 or len(username) > 15:
        return "Must be between 5 and 15 characters."
    else:
        p=list(s.punctuation)
        p.remove('_')
    for i in username:
        if i in p:
            return "Must contain only letters, numbers, or underscores."
    return 'Valid'
def validity(username):
    result=validate(username)
    if result == "Valid":
        print(f"Username '{username}' is valid!")
    else:
        print(f"Username '{username}' is invalid: {result}")
user=input('Username: ')
validity(user)

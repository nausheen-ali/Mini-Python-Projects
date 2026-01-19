import string
import random

characters=list(string.ascii_letters+string.digits+"!@#$%^&*()")

def generate_pw():
    len=int(input("Enter length of password:"))
    random.shuffle(characters)
    password=[]

    for x in range(len):
        password.append(random.choice(characters))

    random.shuffle(password)
    password="".join(password)
    print(password)

choice = input("Generate password? (Y/N)")
if choice.lower()=="y":
    generate_pw()
elif choice.lower()=="n":
    print("Program ended.")
    quit()
else:
    print("Invalid option, please enter Y or N")
    quit()
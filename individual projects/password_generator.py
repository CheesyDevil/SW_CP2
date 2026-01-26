#SW 2nd Password generator


import random

password=[]#list for pass word characters

charopt=[]#list for character options
#makes sure number is a number
def insure():
    while True:
        num=input()
        if f"{num}".isnumeric() and  int(num):
            return int(num)
        else:
                print("Please enter a valid input")
#function for adding uppercase letters
def adup(password):
    password.append(chr(random.randint(65,90)))
    return password
#function for adding lowercase letters
def adlo(password):
    password.append(chr(random.randint(97,122)))
    return password
#function for adding numbers
def adnm(password):
    password.append(chr(random.randint(48,57)))
    return password
#function for adding special characters
def adsp():
    ran=random.randint(1,4)
    if ran==1:
        password.append(chr(random.randint(33,47)))
    elif ran==2:
        password.append(chr(random.randint(58,64)))
    elif ran==3:
        password.append(chr(random.randint(91,96)))
    elif ran==4:
        password.append(chr(random.randint(123,126)))
#function for asking if they want to add a type of character
def ask(string,num,charopt):
    while True:
        inp=input(f"would you like to add {string} to your password (y/n)")
        match inp:
            case "y":
                list(charopt).append(num)
                return charopt
            case "n":
                return 
            case _:
                print("please enter a valid input")
                continue



#function for asking the length and which stuff thay want 
def maine():
    print("how many do you want your password to be?")
    length=insure()
    ask("uppercase letters",1,charopt)
    ask("lowercase letters",2,charopt)
    ask("numbers",3,charopt)
    ask("special characters",4,charopt)



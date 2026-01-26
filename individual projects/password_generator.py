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
def adsp(password):
    ran=random.randint(1,4)
    if ran==1:
        password.append(chr(random.randint(33,47)))
    elif ran==2:
        password.append(chr(random.randint(58,64)))
    elif ran==3:
        password.append(chr(random.randint(91,96)))
    elif ran==4:
        password.append(chr(random.randint(123,126)))
    return password
#function for asking if they want to add a type of character
def ask(string,num,charopt):
    while True:
        inp=input(f"would you like to add {string} to your password (y/n)")
        match inp:
            case "y":
                charopt.append(num)
                return charopt
            case "n":
                return 
            case _:
                print("please enter a valid input")
                continue



#function for asking the length and which stuff thay want 
def maine(charopt,password):
    while True:
        print("how many charcters do you want your password to have?")
        length=insure()
        ask("uppercase letters",1,charopt)
        ask("lowercase letters",2,charopt)
        ask("numbers",3,charopt)
        ask("special characters",4,charopt)
        for i in range(0,length):
            pastring=''
            char=charopt[random.randint(0,(len(charopt)-1))]
            match char: #randomizing when the characters appear
                case 1:
                    adup(password)
                case 2:
                    adlo(password)
                case 3:
                    adnm(password)
                case 4: 
                    adsp(password)
        for i in range(0,len(password)):
            pastring+=password[i]
        print(f"Password:  {pastring}")
        inp=input("would you like to continue creating passwords (y/n)")
        match inp:
            case "y":
                password=[]
                charopt=[]
                continue
            case "n":
                return 
            case _:
                print("please enter a valid input")
                continue

maine(charopt,password)
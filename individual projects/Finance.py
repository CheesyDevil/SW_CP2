#SW 2nd Finantial Calculator

#number ensure function (make sure user input is a number(apply to all other functoins))
def ensure(l,h):
    while True:
        num=input()
        if l and h:
            if f"{num}".isnumeric() and  int(num) in range(l,h):
                return int(num)
            else:
                print("Please enter a valid input")
        else:
            if f"{num}".isnumeric():
                return int(num)
            else:
                print("Please enter a valid input")
#Savings calculator function ((user input for amout to save / user input for amount added) rounded up)user input for weeks or months
def saving():
    print("How much money are you saving up for? ")
    save=ensure()
    print("How much are you depositting?")
    deposit=ensure()
    print("1. Weekly\n2.Monthly\nHow often are you add to account?")
    bol=ensure(1,2)
    if bol==1:
        time="Weeks"
    elif bol==2:
        time="Months"
    else:
        print("ERROR_28")
    if save%deposit:
        print(f"It will take you {(save//deposit)+1} {time} to save up to {save}")
    else:
        print(f"It will take you {save//deposit} {time} to save up to {save}")
    
#compound intrest calculator function (user input for starting amount*((user input for intrest percentage+1)^user input for time)
def compound():
    print('How many catagories do you have?')
    catagory_names=[]
    catagories=ensure()
    for i in range(0,catagories):
        
#budget allocator function (for user input for number of budget catagories: user input for catagories, user input for total budget*user input for the catoagory percentage)

#Sale price function ((1-user input discount%)*user input for origional price)

#Tip calculator function ((user input for tip amount%+1)*user input for item price)

#Starting menu function (user input for which function is used and send user to coresponding function)
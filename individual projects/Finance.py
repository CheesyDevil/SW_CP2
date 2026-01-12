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
def insure():
    while True:
        num=input()
        if f"{num}".isnumeric() and  int(num):
            return int(num)
        else:
                print("Please enter a valid input")
#Savings calculator function ((user input for amout to save / user input for amount added) rounded up)user input for weeks or months
def saving():
    print("How much money are you saving up for? ")
    save=insure()
    print("How much are you depositting?")
    deposit=insure()
    print("1. Weekly\n2.Monthly\nHow often are you add to account?")
    bol=ensure(1,3)
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
    print('How much money was origionally in your account?')
    origional=insure()
    print('What is the interect rate of the account?')
    rate=insure()
    print("HOw many years has the account been compounding?")
    time=insure()
    print(f"after {time} years, your origional {origional} has grown to {((rate+1)^time)*origional}")
        
#budget allocator function (for user input for number of budget catagories: user input for catagories, user input for total budget*user input for the catoagory percentage)
def allcoate():
    catagory_names=[]
    catagory_budget=[]
    print('How many catagories do you have?')
    catagories=insure()
    print("What is your total budget")
    total_budget=insure()
    for i in range(0,catagories):
        name=input(f"What is catagory {i}'s name?\n")
        catagory_names.append[name]
    for i in range(0,catagories):
        print(f"What % of you budget is going in {catagory_names[i-1]}")
        budget=insure()
        catagory_budget.append[budget]
    for i in range(0,catagories):
        print(f"{catagory_names[i-1]}:${((catagory_budget[i-1])/100)*total_budget}")
    
#Sale price function ((1-user input discount%)*user input for origional price)
def sale():
    print("what was the origional price of the item?")
    origional=insure()
    print("What was the dicount?")
    discount=insure()
    print(f'Item costs ${(1-(discount/100))*origional}')
#Tip calculator function ((user input for tip amount%+1)*user input for item price)
def tip():
    print("what was the price of the item?")
    bill=insure()
    print("What percent are you tipping")
    tip=insure()
    print(f'Tip of: ${(tip/100)*bill} and total cost of: ${((tip/100)*bill)+bill}')

#Starting menu function (user input for which function is used and send user to coresponding function)
while True:
    print(f"1:Saving\n2:Compound intrest\n3:Allocate budget\n4:Calculate Sales Price\n5:Calculate Tip\n6:Exit calculator\nWhich option do you want to use?")
    inp=ensure(1,7)
    if inp==1:
        saving()
    elif inp==2:
        compound()
    elif inp==3:
        allcoate()
    elif inp==4:
        sale()
    elif inp==5:
        tip()
    elif inp==6:
        break
print("Thank You for using our Financial calculator")
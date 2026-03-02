#SW 2nd Fractal generator

import turtle as t

screen=t.Screen()


turt=t.Turtle()


def insure():#makes inpu an integer
    while True:
        num=input()
        if f"{num}".isnumeric() and  int(num):
            return int(num)
        else:
                print("Please enter a valid input")

def setup(number):#set up to the nuber is correct
    
    number+=1
    fractal(turt,number)
    turt.fillcolor("red")

def fractal(turt, number):
    number-=1
    for i in range(0,3): #loop so it does all three sides
        turt.right(240)
        turt.forward(20*(2**number)) #move half disttance to check if there is another layer
        if number==0: #base case
            return
        #create new turtle
        clone=turt.clone()
    #have new turtle do fractle function
        fractal(clone, number) #recusion to do the smaller triangles
    
    
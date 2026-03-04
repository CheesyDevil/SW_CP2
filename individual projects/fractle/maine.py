

while True:
    num=input("How many layers would you like the fractal to have")
    if f"{num}".isnumeric() and  int(num):
        x=int(num)
        break
    else:
        print("Please enter a valid input")

import helper as h
h.setup(x)
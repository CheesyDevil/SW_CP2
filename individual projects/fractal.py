#SW 2nd Fractal generator

import turtle as t

screen=t.Screen()


turt=t.Turtle()



def fractal(turt, number):
    number-=1
    for i in range(0,3):
        turt.left(60)
        turt.forward((10*(2**number)))
        if number==0:
            return
        #create new turtle
        clone=turt.clone()
        #have new turtle do fractle function
        fractal(clone, number)
        #move turt 1/2 the distance 
        turt.forward((100/(2**number)))
        #turn 60 degrees
    

fractal(turt,3)
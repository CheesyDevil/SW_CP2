import matplotlib.pyplot as plt
import numpy as np
import math

plt.xlim(-20,20)
plt.ylim(-20,20)



#points 2,3 5, and 6 go 1/2 input to left/down and 1/2 sqrt(3) left/right
#
inp1=int(input("")) #Bottom
inp2=int(input("")) #LBottom
inp3=int(input("")) #Ltop
inp4=int(input("")) #Top
inp5=int(input("")) #RTop   
inp6=int(input("")) #RBottom

plt.fill([0, (-inp2/2)*math.sqrt(3), (-inp2/2)*math.sqrt(3),0,(inp2/2)*math.sqrt(3),(inp2/2)*math.sqrt(3)], [-inp1, (-inp2/2), (inp2/2),inp4,(inp2/2),(-inp2/2)])
plt.plot([0,0], [-20,20], color='r', linestyle='dashed',  linewidth=.7)
plt.plot([-10*math.sqrt(3),10*math.sqrt(3)], [-10,10], color='r', linestyle='dashed',  linewidth=.7)
plt.plot([-10*math.sqrt(3),10*math.sqrt(3)], [10,-10], color='r', linestyle='dashed',  linewidth=.7)
plt.plot([0,-2.5*math.sqrt(3),-2.5*math.sqrt(3),0,2.5*math.sqrt(3),2.5*math.sqrt(3),0], [-5, -2.5, 2.5,5,2.5,-2.5,-5], color='g', linestyle='dashed',  linewidth=.7)
plt.plot([0,-5*math.sqrt(3),-5*math.sqrt(3),0,5*math.sqrt(3),5*math.sqrt(3),0], [-10, -5, 5,10,5,-5,-10], color='g', linestyle='dashed',  linewidth=.7)
plt.plot([0,-7.5*math.sqrt(3),-7.5*math.sqrt(3),0,7.5*math.sqrt(3),7.5*math.sqrt(3),0], [-15, -7.5, 7.5,15,7.5,-7.5,-15], color='g', linestyle='dashed',  linewidth=.7)
plt.plot([0,-10*math.sqrt(3),-10*math.sqrt(3),0,10*math.sqrt(3),10*math.sqrt(3),0], [-20, -10, 10,20,10,-10,-20], color='g', linestyle='dashed',  linewidth=.7)
plt.subplots_adjust(left=None, bottom=None, right=.833, top=1, wspace=None, hspace=None)
plt.show()

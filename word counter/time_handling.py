#SW 2nd Word Counter

#time
import time 
#check time function
    #use time library to check the time
    #return the time

def timecheck(file):
    rtim=time.localtime()
    tim=time.strftime("%Y-%m-%d %H:%M:%S",rtim)
    with open(file, 'a') as txt:
        txt.write(f"\nLast update:{tim}")


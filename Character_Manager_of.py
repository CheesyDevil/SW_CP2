
import random


def roll(choice):
    roll=[]
    for i in int(list(choice)[1]):
        roll.append(random.randint(1,int(list(choice)[3])))
        total+=random.randint(1,int(list(choice)[3]))
    rolls=" ".join(roll)
    print(f"You rolled {rolls} or a total of {total}")    
    
import pandas as pd
import faker
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

class Character:
    def __init__(self,str,dex,con,int,wis,cha,ac,hp,cls):
        self.stats=pd.Series[str,dex,con,int,wis,cha], index=("str","dex","con","int","wis","cha")
        self.ac=ac
        self.inv=dict({})
        self.wep=dict({})
        self.spl=dict({})
        self.equ={"hand_1":'',"hand_2":'',"armour":''}
        self.hp=hp
        self.cls=cls
    def equip(self):
        while True:
            print(f'Hand 1:{self.equ['hand_1']}\nHand 2:{self.equ['hand_2']}\nArmour:{self.equ['armour']}')
            print("Would you like to edit\n1:hands\n2:armour")
            inp=input()
            match inp:
                case "1":
                    print("are you\n1:equiping\n2:stowing")
                    inp=input()
                    match inp:
                        case '1':
                            print("is the item 2 handed?\n1:yes\n2:no")
                            inp=input()
                            match inp:
                                case '1':
                                    print("what are you equiping?")
                                    inp=input()
                                    if self.equ["hand_1"] =="" and self.equ["hand_2"] =="":
                                        self.equ["hand_1"],self.equ["hand_2"] =f"{inp}",f"{inp}"
                                    else:print("your hands ar too full")
                                case '2':
                                    print("what are you equiping")
                                    inp=input()
                                    if self.equ["hand_1"] =="":
                                        self.equ["hand_1"] =f"{inp}"
                                    elif self.equ["hand_2"] =="":
                                        self.equ["hand_2"] =f"{inp}"
                                    else:print("your hands ar too full")
                                case _:
                                    print("please use a valid input")
                        case "2":
                            print(f"What are you stowing\n1:{self.equ['hand_1']}\n2:{self.equ['hand_2']}")
                            inp=input()
                            match inp:
                                case "1":
                                    self.equ["hand_1"]=''
                                case '2':
                                    self.equ["hand_2"]=''
                                case _:
                                    print("please use a valid input")
                        case _:
                            print("please use a valid input")
                    return self.equ
                case "2":
                    print("are you\n1:equiping\n2:dequiping")
                    inp=input()
                    match inp:
                        case "1":
                            print("How heavy is the armour?\n1:light\n2:medium\n3:Heavy")
                            inp=input()
                            if (cls =='rouge' and (inp=="2" or inp=='3')) or cls=='wizard':
                                print("You do not have training in this kind of armour")
                            else:
                                print("what armour are you equiping?")
                                inp=input()
                                if self.equ['armour']=='':
                                    self.equ['armour']=f'{inp}'
                                else:
                                    print("you are already wearing armour")
                        case '2':
                            self.equ['armour']=''
                        case _:
                            print("please use a valid input")
                    return self.equ
                case _:
                    print("please use a valid input")
    def view(self,dictionary,dictname):
        for key in self.select:
            if dictname=="weapons"or"inventory":
                print(f"{key}:{self.select[key][0]}, value:{self.select[key][1]}, weight:{self.select[key][2]}")
            elif dictname=="spells":
                print(f"{key}:{self.select[key][0]}, level:{self.select[key][1]}, casting:{self.select[key][2]}")
    def plus(self,dictionary,dictname):
        name=input(f"What is the name of the item you would like to add to your inventory?\n")
        info=input(f"What is information you would like to give {name}?\n")
        match dictname:
            case "weapons":
                print(f"What is the value of {name}?")
                value=insure()
                print(f"What is the weight of {name}?")
                weight=insure()
                self.select[name]=[info,value,weight]
                print(f"{name} added to inventory")
            case "inventory":
                print(f"What is the value of {name}?")
                value=insure()
                print(f"What is the weight of {name}?")
                weight=insure()
                self.select[name]=[info,value,weight]
                print(f"{name} added to inventory")
            case "spells":
                print(f"What level of spell is {name}?")
                spellev=insure()
                time=input(f"What is the casting time of {name}?\n")
                self.select[name]=[info,spellev,time]
                print(f"{name} added to inventory")
        return self.select
    def minus(self,dictionary):
        print("Note: If you remove it you will have to manually add it back!")
        name=input(f"Which item would you like to remove from your inventory?\n")
        if name in self.select:
            del self.select[name]
            print(f'{name} has been removed')
        else:
            print(f"{name} wasn't found in inventory")
        return self.select
    def search_dict(self,dictionary):
        key=list(dict(self.select).keys())
        print("How would you like to search your inventory\n1. name\n2. feature")
        bol=ensure(1,3)
        inp=input("What are you searching for?\n")
        if bol==1:
            if inp in self.select:
                print(f"{inp}:{self.select[inp][0]}, value:{self.select[inp][1]}, weight:{self.select[inp][2]} ")
            else:
                print(f"{inp} not in inventory")
        if bol==2:
            for i in range(0,len(key)):
                if f'{inp}' in self.select[key[i]][0]:
                    print(f"{key[i]}:{self.select[key[i]][0]}, value:{self.select[key[i]][1]}, weight:{self.select[key[i]][2]}")
                else:
                    continue
    def edit(self,dictionary,dictname):
        while True:
            print(f"1:View \n2:add to \n3:remove \n4:search for specific name/attribute\n5:Exit editor\nWhich option do you want to use?")
            inp=ensure(1,6)
            if inp==1:
                self.view(dictionary,dictname)
            elif inp==2:
                self.plus(dictionary,dictname)
            elif inp==3:
                self.minus(dictionary)
            elif inp==4:
                self.search_dict(dictionary)
            elif inp==5:
                break
        return dictionary
    def choice(self):
        print(f"What would you like to edit?\n1:weapons\n2:inventory")
        if self.cls=='wizard':
            print("3:spells")
            inp=ensure(0,3)
        else:
            inp=ensure(0,2)
        match inp:
            case 1:
                self.select=self.wep
            case 2:
                self.select=self.inv
            case 3:
                self.select=self.spl
                

class Pet:    
    def __init__(self, name, species, age=0, health=100, hunger=100, happiness=100, energy=100, skills=[]):
        self.name=name.capitalize()
        self.species=species.title()
        self.age=0
        self.health=100
        self.hunger=100
        self.happiness=100
        self.energy=100
        self.skills=[]
    def __str__(self):
        he=bar(self.health)
        hu=bar(self.hunger)
        ha=bar(self.happiness)
        en=bar(self.energy)
        return f"Name: {self.name}\nSpecies: {self.species}\nAge: {self.age}\nHealth: [{he}] {self.health}%\nHunger: [{hu}] {self.hunger}%\nHappiness: [{ha}] {self.happiness}%\nEnergy: [{en}] {self.energy}%\nSkills: {self.skills}"

pets=dict({})

#Change stat function(Health, Level, Health, Hunger, Happiness, Energy)

def bar(inp):
    out=""
    nip=inp/5
    for i in range(10):
        if nip > i:
            out=out+"█"
        else:
            out=out+"░"
    return out

#time passing
    #covert hours to days and over time increase pet age
def time(cmonth,cday,chour,hours):
    nhour=chour+hours
    if nhour>24:
        nhour-=24
        bday=cday+1
    else:
        nday=cday
    if bday==30:
        nmonth=cmonth+1
        nday=0
    else:
        nday=bday
        nmonth=cmonth
    return [nhour,nday,nmonth]


#Feed
    #Buy From Food options
    #increase stat function
    # return To menu

#play
    #choose how long you play for
    #increase happiness and health
    #decrease energy

#Put to Sleep
    #choose how long you nap for
    #increase Energy and health
    #decrease Hunger

#Check status
    #Bar Graph Function
    #print out name, species, age, Level, Health, Hunger, Happiness, Energy, Skills
    

#Pet management
    #return to pet select 
#Create new Pet (in a class)
def newpet():
    name=input(f"What would you like to name your pet: ")
    while True:
        inp=input(f"Select pet\n[1] Cat\n[2] Dog\n[3] Horse\n[4] Fish\n[5] Hampster\n[6] Guinea Pig\n[7] Bunny\n[8] Unicorn\n[9] Pegasus\n[10] Dragon")
        match inp:
            case '1':
                species='Cat'
                break
            case '2':
                species='Dog'
                break
            case '3':
                species='Horse'
                break
            case '4':
                species='Fish'
                break
            case '5':
                species='Hampster'
                break
            case '6':
                species='Guinea Pig'
                break
            case '7':
                species='Bunny'
                break
            case '8':
                species='Unicorn'
                break
            case '9':
                species='Pegasus'
                break
            case '10':
                species='Dragon'
                break
            case _:
                print("please enter a valid input\n")
                continue
    pets[name]=Pet(name,species)
    print(pets[name])
    #Switch pet
    #Release pet
    #return to Main Menu

#Save
    #save stats to the pet's area of save file

#Load
    #takes The pet info and opens it
newpet()
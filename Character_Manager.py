# !-is used to take and action/use an ability  ?-is used to get info on the action/ablity/item 
import random

#Lists
hands=[]
#strings
choice=""
#dictionaries
weapons={
'Club':["1d4","Bludgeoning","Strength","Slow","Light",2],
'Dagger':["1d4","Piercing","Finesse(Str or Dex)","Nick","Light","Throwable (20/60)",1],
'Greatclub':["1d8","Bludgeoning","Strength","Push","Two-Handed",10],
'Handaxe':["1d6","Slashing","Strength","Vex","Light","Throwable (20/60)",2],
'Javelin':["1d6","Piercing","Strength","Slow","Throwable (30/120)",2],
'Light Hammer':["1d4","Bludgeoning","Strength","Nick","Light","Throwable (20/60)",2],
'Mace':["1d6","Bludgeoning","Strength","Sap",4],
'Quarterstaff':["1d6 or 1d8 in both hands","Bludgeoning",'Strength',"Topple",4],
'Sickle':["1d4","Slashing","Strength","Nick","Light",2],
'Spear':["1d6","Piercing",'Strength',"Sap","Versitile (1d8)","Throwable (20/60)",3],

'Dart':["1d4","Piercing","Finesse(Str or Dex)","Vex","Throwable (20/60)",0.25],
'Light Crossbow':["1d8","Piercing","Dexterity","Slow","Ammunition (80/320); Bolt","Loading","Two-Handed",5],
'Shortbow':["1d6","Piercing","Dexterity","Vex","Ammunition (80/320); Arrow","Two-Handed",2],
'Sling':["1d4","Bludgeoning","Dexterity","Slow","Ammunition (80/320); Shot",0],

'Battleaxe':["1d8 or 1d10 in both hands","Slashing",'Strength',"Topple",4],
'Flail':["1d6","Bludgeoning",'Strength',"Sap",2],
'Glaive':["1d10","Slashing",'Strength',"Graze","Heavy","Reach","Two-Handed",6],
'Greataxe':["1d12","Slashing",'Strength',"Cleave","Heavy","Two-Handed",7],
'Greatsword':["2d6","Slashing",'Strength',"Graze","Heavy","Two-Handed",6],
'Halberd':["1d10","Slashing",'Strength',"Cleave","Heavy","Reach","Two-Handed",6],
'Lance':["1d10","Piercing",'Strength',"Topple","Heavy","Reach","Two-Handed (unless mounted)",6],
'Longsword':["1d8","Slashing",'Strength',"Sap","Versitile (1d10)",3],
'Maul':["2d6","Slashing",'Strength',"Topple","Heavy","Two-Handed",10],
'Morningstar':["1d8","Piercing",'Strength',"Sap",4],
'Pike':["1d10","Piercing",'Strength',"Push","Heavy","Reach","Two-Handed",18],
'Rapier':["1d8","Slashing",'Finesse (Str or Dex)',"Vex",2],
'Scimitar':["1d6","Slashing",'Finesse (Str or Dex)',"Nick","Light",3],
'Shortsword':["1d6","Piercing",'Finesse (Str or Dex)',"Vex","Light",2],
'Trident':["1d8 or 1d10 in both hands","Piercing",'Strength',"Topple","Thrown (20/60)",4],
'Warhammer':["1d8 or 1d10 in both hands","Bludgeoning",'Strength',"Push",5],
'War Pick':["1d8 or 1d10 in both hands","Piercing",'Strength',"Sap",2],
'Whip':["1d4","Slashing",'Finesse (Str or Dex)',"Slow","Reach",3],

'Blowgun':["1d1","Piercing","Dexterity","Vex","Ammunition (25/100); Needle","Loading",1],
'Hand Crossbow':["1d6","Piercing","Dexterity","Vex","Ammunition (30/120); Bolt","Loading","Light",3],
'Heavy Crossbow':["1d10","Piercing","Dexterity","Push","Ammunition (100/400); Bolt","Loading","Two-Handed","Heavy",18],
'Longbow':["1d8","Piercing","Dexterity","Slow","Ammunition (150/600); Arrow",'Heavy',"Two-Handed",2],
'Musket':["1d12","Piercing","Dexterity","Slow","Ammunition (40/120); Bullet","Loading","Two-Handed",10],
'Pistol':["1d10","Piercing","Dexterity","Vex","Ammunition (30/90); Bullet","Loading",3],
}

def roll(weapon,hands,choice):
    if "Two-Handed" in weapon[choice] and hands[0]==hands[1] and len(weapon[choice])<5:
        if weapon!="Quarterstaff":
            dmg=random.randint(1,10)
        else:
            dmg=random.randint(1,8)
    else:
        for i in list(weapon[choice])[0]:
            dmg+=random.randint(1,int(list(weapon[choice])[2]))
    print(f"You dealt {dmg} {weapon[choice][1]} damage")

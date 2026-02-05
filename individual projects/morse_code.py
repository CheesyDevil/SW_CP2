#SW 2nd Simple morse code translator


morse=("-.",'...-','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..')#tuple for morse code characters
english=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')#tuple for English characters

def mte():#function for asking for input to translate from morse code to english
#loop turning each character into thhier coresponding
    inp=input("what would you like to translate?\n")
    lit=inp.split()
    fin=""
    for item in lit:
        if item in morse:
            ind=morse.index(item)
            fin+=english[ind]
        else:  
            return print("\nPlease only input periods, hyphons and spaces\n")
    print(f"\nYour message is:{fin}\n")


def etm():#function for asking for input to translate from english to morse code
    #loop turning each character into thhier coresponding
    inp=input("what would you like to translate?\n").lower()
    lit=list(inp)
    if " " in lit:
        lit.remove(" ")
    fin=""
    for item in lit:
        if item in english:
            ind=english.index(item)
            fin+=f"{morse[ind]} "
        else:  
            return print("\nPlease only input english characters\n")
    print(f"\nYour message is:{fin}\n")

#main loop for asking which function they want to do
def maine():
    while True:
        inp=input("what would you like to do?\n1:Morse code to English\n2:English to morse code\n3:Exit\n")
        match inp:
            case "1":
                mte()
            case '2':
                etm()
            case "3":
                break
            case _:
                print('\nplease enter on of the listed numbers')
                continue
    print('\nThank you for using this morse code program')

maine()
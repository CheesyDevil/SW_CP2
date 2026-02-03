#SW 2nd Simple morse code translator


morse=("-.",'...-','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..')#tuple for morse code characters
english=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')#tuple for English characters

def mte():#function for asking for input to translate from morse code to english
#loop turning each character into thhier coresponding
    inp=input("what would you like to translate?")
    lit=inp.split()
    fin=""
    i=0
    for item in lit:
        char=lit.index(item)
        if char in morse:
            i+=1
            ind=morse.index(char)
            fin+=english.index(ind)
            if i==len(lit):
                print(f"Your message is:{fin}")
        else:
            break
        print("Please only input periods, hyphons and spaces")


#function for asking for input to translate from english to morse code
    #loop turning each character into thhier coresponding

#main loop for asking which function they want to do
mte()
#SW 2nd Word Counter


#readtxt function
    #open inputted file in "r" mode
    #initialize wordcount vairable as empy integer
    #for lines in inputted file
        #use split function to split up words
        #use len function to get length of list
        #add the length to word count
    #output wordcount

#write function
    #open inputted file in "a" mode
    #forever loop
        #ask user fo rline to add to the file
        #append inputted line to the file
        #ask user if they want to add anything alse
        #if yes contnue loop
        #else leave loop
    #return

#view function
    #open inputted file in "r" mode 
    #for lines in inputted file
        #print line
    #return

def setup(file):
    try:
        with open (file,'a') as txt:
            txt.write('\n')
            txt.write('\n')
            txt.write('\n')
    except:
        file=""
        return file

def deletetime(file):
    updates=[]
    with open(file, 'r') as txt:
        lines=txt.readlines()
    with open (file,'w') as txt:
        txt.writelines(lines[:-2])
    return updates

def wrdcnttxt(file):
    x=deletetime(file)
    try:
        x=deletetime(file)
        with open(file, 'r') as txt:
            wordcount=0
            for line in txt:
                line.split()
                wordcount+=len(line)
        with open(file,'a') as txt:
            txt.write(f"\n")
            txt.write(f"Word Count:{wordcount}\n")
        return x
    except:
        print("please enter a valid file")

#write function
def writetxt(file):
    try:
        with open(file, 'a') as txt:
            while True:
                nline=input("What would you like to add to your file?")
                txt.write(f"{nline}\n")
                inp=input(f"would you like to continue (y/n)")
                while True:
                    if inp!="y"and inp!='n':
                        print("please enter a valid input")
                    else:
                        break
                match inp:
                    case 'y':
                        continue
                    case 'n':
                        break
            return
    except:
        print("please enter a valid file")


def viewtxt(file):
    try:
        with open(file,'r') as txt:
            content=[]
            for line in txt:
                content.append(line.strip())
    except:
        print("File Not Found")
    else: 
        print("Document Content:\n")
        for line in content:
            print(line)

def select(file):
    while True:
        inp=input("what would you like to like to do to your file \n1: View\n2: Edit\n3: Check Word Count\n4: Exit")
        match inp:
            case "1":
                viewtxt(file)
            case "2":
                deletetime(file)
                writetxt(file)
                wrdcnttxt(file)

            case '3':
                wrdcnttxt(file)
            case '4':
                break
            case _:
                continue
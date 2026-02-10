#SW 2nd Moviw recomender


#import csv
import csv


opt=["Title","Genre","Rating","Director","Actor","Length"]
movies=[]




#read csv function(function turning each line into a dictionary)
def read(movies):
    with open("individual projects\\Movies list - Sheet1 (1).csv",mode="r") as sample:
        read=csv.reader(sample)
        header=next(read)
        movies=[]
        for line in read:
            movies.append(
                {
                    header[0]:line[0],
                    header[1]:line[1],
                    header[2]:line[2],
                    header[3]:line[3],
                    header[4]:line[4],
                    header[5]:line[5]
                }
            )
    return  movies





#Search/recomendations function(parameter for what they are looking for)
def search(inp):
    inp.split(",")
    #Turn imputted filters into a list 

    #Loop for each number in the list
    results=[]
    for o in inp:
        inpu=input(f"what are you looking for in {opt[o-1]}")
        read(movies)
        if o==6:
            while True:
                ip=input("Do you want\n1: maximum length\n2:minimum length")
                if ip=='1' or ip=='2':
                    break
                else:
                    print('please enter either a 1 of a 2')
                    continue
        for i in movies:
            if o<=5:
                if inpu in i[o-1]:
                    results.append(i)
            elif o==6:
                int(inpu)
                match ip:
                    case "1":
                        if inpu < i[o-1]:
                            results.append(i)
                    case "2":
                        if inpu>i[o-1]:
                            results.append(i)
                    case _:
                        print("ERROR")
                        continue

        #ask for the name of the thing they are searching
        #Check the dictionaries to find a valid one
        #if there is a valid add it's title to a list
    #check all the lists for overlap and print those titles

#print full movie list function(use the read function and print out the dictionaries)

#main(put the functions to together)

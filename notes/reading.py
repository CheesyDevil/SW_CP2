import csv

'''try:
    with open('notes\\sample.txt',"r") as file:
        content=[]
        for line in file:
            content.append(line.strip())
except:
    print("File Not Found")
else: #Else happens WITH try
    for line in content:
        print('hello',line)'''


try:
    with open("SW_CP2\\notes\\Class CSV sample - Sheet1.csv",mode='r') as sample:
        read=csv.reader(sample)
        header=next(read)
        users=[]
        for line in read:
            users.append(
                {
                    header[0]:line[0],
                    header[1]:line[1]
                }
            )
except:
    print("not found")
else:
    for user in users:
        print(user)
    print(users[1]['username'])
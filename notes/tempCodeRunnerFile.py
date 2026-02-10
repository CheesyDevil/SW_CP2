try:
    with open('notes\\sample.txt',"r") as file:
        content=[]
        for line in file:
            content.append(line.strip())
except:
    print("File Not Found")
else: #Else happens WITH try
    for line in content:
        print('hello',line)
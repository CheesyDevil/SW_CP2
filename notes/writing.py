#SW 2nd Writing to file notes

with open('SW_CP2\\notes\\write_to_file.txt','a') as file:
    file.write('\nme')
    file.write('\nmyself')
    file.write('\nI')
print("finished")

'''content=[]
with open('notes\\write_to_file.txt','r+') as file:
    for line in file:
        content.append(line.strip())

    index=content.index("I")
    content[index]="seth"

    file.truncate(0)

    for name in content:
        file.write(name+"\n")
print("code ends")'''


import csv

users=[{'username':"user1","favorite color":'red'},{'username':"user2","favorite color":'green'},{'username':"user3","favorite color":'blue'}]
with open("notes\\test.csv", 'r+' , newline='') as csvfile:
    fieldnames=["username","favorite color"]
    reader=csv.reader(csvfile)
    writer=csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writerow(fieldnames)
    writer.writerows(users)





#"r" for read
#"w" for write
#'a' for append
#'r+' for read/write

import csv

def save(pets):
    users=[{'1':name,"2":species,'3':age,"4":health,'5':happiness,'6':hunger,'7':energy},{'1':name,"2":species,'3':age,"4":health,'5':happiness,'6':hunger,'7':energy},{'1':name,"2":species,'3':age,"4":health,'5':happiness,'6':hunger,'7':energy},{'1':name,"2":species,'3':age,"4":health,'5':happiness,'6':hunger,'7':energy},{'1':name,"2":species,'3':age,"4":health,'5':happiness,'6':hunger,'7':energy},{'1':name,"2":species,'3':age,"4":health,'5':happiness,'6':hunger,'7':energy},{'1':name,"2":species,'3':age,"4":health,'5':happiness,'6':hunger,'7':energy},{'1':name,"2":species,'3':age,"4":health,'5':happiness,'6':hunger,'7':energy},{'1':name,"2":species,'3':age,"4":health,'5':happiness,'6':hunger,'7':energy},{'1':name,"2":species,'3':age,"4":health,'5':happiness,'6':hunger,'7':energy},{'1':kibble,"2":premiumkibble,'3':fish,"4":steak}{'1':money}]
    with open("notes\\test.csv", 'r+' , newline='') as csvfile:
        fieldnames=["1","2",'3','4']
        reader=csv.reader(csvfile)
        writer=csv.DictWriter(csvfile, fieldnames=fieldnames)

        #writer.writerow(fieldnames)
        writer.writerows(users)

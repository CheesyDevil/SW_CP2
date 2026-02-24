#SW 2nd Word Counter
import file_handling as h
import time_handling as t

while True:
    file=input("Please enter the exact file path for your document")
    h.setup(file)
    if file:
        while True:
            inp=input("what would you like to like to do to your file \n1: View\n2: Edit\n3: Check Word Count\n4: Exit\n")
            match inp:
                case "1":
                    h.viewtxt(file)
                case "2":
                    h.deletetime(file)
                    h.writetxt(file)
                    h.wrdcnttxt(file)
                    t.timecheck(file)
                case '3':
                    h.deletetime(file)
                    h.wrdcnttxt(file)
                    t.timecheck(file)
                    h.viewtxt(file)
                case '4':
                    break
                case _:
                    continue
    else:
        continue

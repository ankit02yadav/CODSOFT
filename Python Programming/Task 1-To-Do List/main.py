import csv,os,datetime

class Const:
     TaskFile = "TaskFile.csv"
    
def main():
    while(True):
        print("\033[94m/////////// Welocome to To-Do List App /////////////");
        print("1. View Your To-Do List");
        print("2. Add a Task")
        print("3. Remove any Task");
        print("4. Update Task Status");
        print("5. Track Your Task");
        print("6. Exit;")
        try:
            a = int(input("Enter Your Choice : "))
            if(a==1):
                ViewTask();
            elif(a==2):
                AddTask();
            elif(a==3):
                RemoveTask();
            elif(a==4):
                UpdateStatus();
            elif(a==5):
                Track();
            else:
                break;
        except:
            print("Invalid Choice \n");     
def CheckFile(filename):
    try:
        file = open(filename, "r") 
        file.close()  
        return 1  
    except:
        file = open(filename, "w")
        file.close()
        return 1   
def ViewTask():
    CheckFile(Const.TaskFile);
    file = open(Const.TaskFile,"r")
    csvreader = csv.reader(file);
    line=0;
    for data in csvreader:
        line = line + 1 ;
        print(f"\033[91m{line} {data[0]},{data[2]}\033[94m");
def RemoveTask():
    ViewTask();
    try:
        n = int(input("Which Task you want to remove : "));
        print("Removing.....")
        file = open(Const.TaskFile,"r");
        temp_file = open("tempfile.csv","w",newline='');
        csvreader = csv.reader(file);
        csvwriter = csv.writer(temp_file)
        line = 0;
        for data in csvreader:
            line = line + 1;
            # print(line)
            try: 
                if(line == n):
                    print("Found")
                    fount = 1;
                    continue;
            except:
                passed = 0;
            csvwriter.writerow(data)
            # print("hhhh")
            
        if(fount == 1):
            file.close();
            temp_file.close()
            print("Removed")
            os.remove("TaskFile.csv")
            os.rename("tempfile.csv","TaskFile.csv")
        else:
            os.remove("tempfile.csv")
                
    except:
        print("Invalid Input");
def DateAndTime():
    CurrentTime = datetime.datetime.now()
    return CurrentTime;
def AddTask():
    CheckFile(Const.TaskFile)
    task = input("Enter Your Task : ");
    status = "Pending"
    print(f"{status} - by deafult")
    file = open(Const.TaskFile,"a",newline='');
    csvwriter = csv.writer(file);
    date = DateAndTime();
    data = [task,date,status]
    print(data)
    csvwriter.writerow(data);
    file.close();
def UpdateStatus():
    ViewTask();
    n = int(input("Which Task Status you want to change : "))
    file = open(Const.TaskFile,"r");
    print("Processing...")
    temp_file = open("tempfile.csv","w",newline='');
    csvreader = csv.reader(file);
    csvwriter = csv.writer(temp_file)
    line = 0;
    for data in csvreader:
        line = line + 1;
        
        # print(line)
        try: 
            if(line == n):
                print("Found")
                if(data[2]=="Pending"):
                    newstatus="Completed"
                else:
                    newstatus="Pending";
                updatedata = [data[0],data[1],newstatus]
                csvwriter.writerow(updatedata);
                fount = 1;
                continue;
        except:
            passed = 0;
        csvwriter.writerow(data)
        # print("hhhh")
            
    if(fount == 1):
        file.close();
        temp_file.close()
        print("Updated")
        os.remove("TaskFile.csv")
        os.rename("tempfile.csv","TaskFile.csv")
    else:
        os.remove("tempfile.csv")
def Track():
    CheckFile(Const.TaskFile);
    file = open(Const.TaskFile,"r")
    csvreader = csv.reader(file);
    line=0;
    for data in csvreader:
        line = line + 1 ;
        if(data[2]=="Pending"):
            print(f"\033[91m{line} {data[0]},{data[1]},{data[2]}\033[94m");
main();

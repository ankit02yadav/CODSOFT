import csv,os
class Const:
    ContactFile = "ContactFile.csv";
    
def main():
    while(True):
        print("############### Contact Book ###############")
        print("1. View All Contacts ")
        print("2. Add Contact")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Exit")
        try:
            choice = int(input("Enter your Choice : "))
            if(choice==1):
                ViewContacts();
            elif(choice==2):
                AddContact();
            elif(choice==3):
                DeleteContact();
            elif(choice==4):
                UpdateContact();
            elif(choice==5):
                print("really..");
                return 0;
            else:
                print("Invalid Input")
                return 0;
        except:
            print("Invalid Input")
            return 0;
def CheckFile(filename):
    try:
        file = open(filename,"r")
        file.close()
        return 1;
    except:
        file = open(filename,"w")
        file.close()
        return 1;
def ViewContacts():
    CheckFile(Const.ContactFile)
    file = open(Const.ContactFile,"r")
    csvreader = csv.reader(file)
    for data in csvreader:
        for i in data:
            print(f"{i:10}",end=" ");
        print("")
def AddContact():
    name = input("Enter Name : ")
    phNo = int(input("Enter Phone Number : "))
    email = input("Enter Email : ")
    Address = input("Enter Address : ")
    data = [name,phNo,email,Address]
    # print(data)
    file = open(Const.ContactFile,"a",newline='')
    csvwriter = csv.writer(file)
    csvwriter.writerow(data);
    file.close();
def DeleteContact():
    found = False;
    deleteNumber = input("Enter Phone Number of the contact you want to delete : ")
    CheckFile(Const.ContactFile)
    file = open(Const.ContactFile,"r")
    tempfile = open("tempfile.csv","w",newline='')
    csvreader = csv.reader(file)
    csvwriter = csv.writer(tempfile)

    for data in csvreader:
        if(data[1]==deleteNumber):
            found = True
            print("deleted")
        else:
            csvwriter.writerow(data)
    file.close();
    tempfile.close();
    if(found):
        print("Contact Removed")
        os.remove("ContactFile.csv")
        os.rename("tempfile.csv","ContactFile.csv")
        return 0;
    else:
        print("Contact Not Found ")
        os.remove("tempfile.csv")
        return 0;
def UpdateContact():
    checknumber = input("Enter phone number of the contact you want to update  : ")
    readfile = open(Const.ContactFile, "r")
    csvreader = csv.reader(readfile)
    tempfile = open("tempfile.csv", "w", newline='')
    csvwriter = csv.writer(tempfile)

    found = False
    for data in csvreader:
        if(data[1] == checknumber):
            name = input("Enter Name : ")
            email = input("Enter Email : ")
            Address = input("Enter Address : ")
            newdata = [name, data[1], email, Address]
            csvwriter.writerow(newdata)
            found = True
        else:
            csvwriter.writerow(data)

    readfile.close()
    tempfile.close()

    if found:
        os.remove(Const.ContactFile)
        os.rename("tempfile.csv", Const.ContactFile)
        print("Contact updated successfully.")
    else:
        os.remove("tempfile.csv")
        print("Contact not found.")

main();



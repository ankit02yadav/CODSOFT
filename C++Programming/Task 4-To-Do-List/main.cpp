#include <bits/stdc++.h>
using namespace std;
string Taskfile = "ToDoList.csv";
int CheckFile(string filename);
int ViewTask();
int AddTask();
int RemoveTask();
int UpdateTask();

int main(){
    CheckFile(Taskfile);
    while (1)
    {
        int choice;
        cout<<"############ To Do List ############"<<endl;
        cout<<"1. View Task List"<<endl;
        cout<<"2. Add Task"<<endl;
        cout<<"3. Update Status"<<endl;
        cout<<"4. Remove Task"<<endl;
        cout<<"Enter Your Choice : ";
        cin>>choice;
        switch (choice)
        {
        case 1:
            ViewTask();
            break;
        case 2:
            AddTask();
            break;
        case 3:
            UpdateTask();
            break;
        case 4:
            RemoveTask();
            break;
        
        default:
            break;
        }
    }
    
}
int CheckFile(string filename){
    ofstream file(filename,ios::app);
    file.close();
    return 1;
}
int ViewTask(){
    ifstream file(Taskfile);
    string line;
    string task,status;
    int countLine = 0;
    while (getline(file,line))
    {
        countLine += 1;
        cout<<countLine<<". "<<line<<endl;
    }
    
}
int AddTask(){
    CheckFile(Taskfile);
    ofstream file(Taskfile,ios::app);
    string task ;
    string status = "Pending";
    cout<<"Enter Your Task : ";
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Flush the buffer
    getline(cin,task);
    file<<task<<","<<status<<endl;
    cout<<"By Default the status is pending change it from menu"<<endl;
    file.close();
}
int RemoveTask(){
    ViewTask();
    int n;
    cout<<"Which Task You Want To Remove : ";
    cin>>n;
    ofstream tempfile("temp.csv");
    ifstream file(Taskfile);
    string line;
    int found = 0;
    int lineCount = 0;
    while (getline(file,line))
    {
        lineCount +=1;
        if(lineCount == n){
            continue;
        }
        else{
            tempfile<<line<<endl;
            found=1;
        }
    }
    file.close();
    tempfile.close();
    if(found==1){
        cout<<"Removed successfully"<<endl;
        remove("ToDoList.csv");
        rename("temp.csv","ToDoList.csv");
        return 0;
    }
    else{
        remove("temp.csv");
        return 0;
    }
    
}
int UpdateTask(){
    ViewTask();
    int n;
    cout<<"Which Task You Want To Update : ";
    cin>>n;
    ofstream tempfile("temp.csv");
    ifstream file(Taskfile);
    string line;
    int found = 0;
    int lineCount = 0;
    while (getline(file,line))
    {
        lineCount +=1;
        if(lineCount == n){
            string task,status;
            stringstream ank(line);
            getline(ank, task, ',');
            getline(ank, status);
            if(status == "Pending"){
                tempfile<<task<<",Completed"<<endl;
            }
            else{
                tempfile<<task<<",Pending"<<endl;
            }
        }
        else{
            tempfile<<line<<endl;
            found=1;
        }
    }
    file.close();
    tempfile.close();
    if(found==1){
        cout<<"Status Changed successfully"<<endl;
        remove("ToDoList.csv");
        rename("temp.csv","ToDoList.csv");
        return 0;
    }
    else{
        remove("temp.csv");
        return 0;
    }
}
#include <bits/stdc++.h>
using namespace std;
int main(){
    float num1,num2;
    int Choice;
    try{
        cout<<"Enter First Number : ";
        cin>>num1;
        cout<<"Enter Second Number : ";
        cin>>num2;
        cout<<"Choose Your Operator"<<endl;
        cout<<"1. Addition (+)"<<endl;
        cout<<"2. Subtraction (-)"<<endl;
        cout<<"3. Multiplication (*)"<<endl;
        cout<<"4. Division (/)"<<endl;
        cout<<"Enter Your Choise (1/2/3/4) : ";
        cin>>Choice;
        switch (Choice)
        {
        case 1:
            cout<<"Addition of "<<num1<<" and "<<num2<<" is "<<num1+num2;
            break;
        case 2:
            cout<<"Subtraction of "<<num1<<" and "<<num2<<" is "<<num1-num2;
            break;
        case 3:
            cout<<"Multiplication of "<<num1<<" and "<<num2<<" is "<<num1*num2;
            break;
        case 4:
            cout<<"Division of "<<num1<<" and "<<num2<<" is "<<num1/num2;
            break;
        
        default:
            break;
        }
    }
    catch(errc){
        return 0;
    }
}
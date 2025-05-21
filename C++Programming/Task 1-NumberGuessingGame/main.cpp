#include <bits/stdc++.h>
using namespace std;

void print(string STRING){
    cout<<STRING<<endl;
}
int game(int number){
    while (1)
    {
        int userinput ;
        cout<<"Guess Your Number Between 1 to 100 : ";
        cin>>userinput;
        if(userinput>number){
            print("Big Number Guess Again");
        }
        else if(userinput<number){
            print("Small Number Guess Again");
        }
        else{
            print("Well Done You Got It Right ");
            return 0;
        }

    }
}
int main(){
    srand(time(0));
    int number = rand() % 100 + 1;  // 1 to 100
    print("#### Welcome To Number Gussing Game ####");
    game(number);
}
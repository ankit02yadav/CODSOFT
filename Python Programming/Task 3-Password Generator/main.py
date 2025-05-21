import string,random
AllLetters = list(string.ascii_lowercase + string.ascii_uppercase);
AllNumbers = list(string.digits);
AllSymboles = list(string.punctuation);
def PasswordGenerator():
    try:
        length = int(input("Enter Length Of Password : "))
        if(length<=4):
            print("Password less than 5 is weak increase length")
            return 0 ;
        LettersLength = length // 2
        DigitsLength = length // 4
        SymbolesLength = length - (LettersLength + DigitsLength)
        Letters = random.choices(AllLetters,k=LettersLength)
        Digits = random.choices(AllNumbers,k=DigitsLength)
        Symboles = random.choices(AllSymboles,k=SymbolesLength)
        password = Letters + Symboles + Digits
        random.shuffle(password)
        password = ''.join(password)
        print(password)
    except:
        print("Invalid Input")
        return 0;
PasswordGenerator();
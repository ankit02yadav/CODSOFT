def calculator():
    print("####Welcome to the Simple Calculator####");
    try:
        num1 = float(input("Enter the first number: "));
        num2 = float(input("Enter the second number: "));
    except:
        print("Invalid input. Please enter numeric values.");
        return 0;

    print("What you want to do");
    print("1. Addition +");
    print("2. Subtraction -");
    print("3. Multiplication X");
    print("4. Division /");
    
    choice = input("Enter your choice : ");

    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.");
            return 0;
        result = num1 / num2
    else:
        print("Invalid operation choice.")
        return 0;
    print(f"\nResult : {result}");
calculator();
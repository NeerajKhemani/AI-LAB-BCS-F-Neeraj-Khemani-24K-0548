while True:
    print("\n")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a1 = int(input("Enter first number: "))
        a2 = int(input("Enter second number: "))
        print("Result:", a1 + a2)

    elif choice == 2:
        a1 = int(input("Enter first number: "))
        a2 = int(input("Enter second number: "))
        print("Result:", a1 - a2)

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid input.")

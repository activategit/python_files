op = str(input("Enter the character according to this table\n1. + for Addition\n2. - for Subtraction\n3. * for multiplication\n4. / for division\nOperation = "))
if op == ("+"):
    num1 = float(input("You have chosen addition\nEnter a number = "))
    num2 = float(input("\nEnter a another number = "))
    result = num1 + num2
    result = float(result)
    print(str(num1) + " + " + str(num2) + " = " + str(result))
if op == ("-"):
    num1 = float(input("You have chosen subtraction\nEnter a number = "))
    num2 = float(input("\nEnter a another number = "))
    result = num1 - num2
    result = float(result)
    print(str(num1) + " - " + str(num2) + " = " + str(result))
if op == ("*"):
    num1 = float(input("You have chosen multiplication\nEnter a number = "))
    num2 = float(input("\nEnter a another number = "))
    result = num1 * num2
    result = float(result)
    print(str(num1) + " * " + str(num2) + " = " + str(result))
if op == ("/"):
    num1 = float(input("You have chosen division\nEnter a number = "))
    num2 = float(input("\nEnter a another number = "))
    result = num1 / num2
    result = float(result)
    print(str(num1) + " / " + str(num2) + " = " + str(result))
else:
    print("That's not a operation")

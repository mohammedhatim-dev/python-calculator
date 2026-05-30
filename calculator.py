first_number = input("Enter your first number: ")
operator = input("Enter operator (+, -, *, /): ")
second_number = input("Enter your second number: ")

try:
    
    first_number = float(first_number)
    second_number = float(second_number)

    
    if operator == "+":
        print(f"Result: {first_number + second_number}")
    elif operator == "-":
        print(f"Result: {first_number - second_number}")
    elif operator == "*":
        print(f"Result: {first_number * second_number}")
    elif operator == "/":
      
        if second_number == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {first_number / second_number}")
    else:
        print("Error: Invalid operator. Please use +, -, *, or /.")

except ValueError:
   
    print("Error: Invalid input! Please enter valid numeric values.")

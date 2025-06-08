x = int(input("enter the number: "))
y = int(input("enter the number:"))

operation = input("enter the operation you want to perform: ")
match operation:
    case "add":
        print(f"the sum of {x} and {y} is {x+y}")
    case "sub":
        print(f"the difference of {x} and {y} is {x-y}")
    case "mul":
        print(f"the product of {x} and {y} is {x*y}")
    case "div":
        if y != 0:
            print(f"the division of {x} and {y} is {x/y}")
        else:
            print("Error: Division by zero is not allowed.")
    case "sqr":
        if x > 0:
            print(f"The square root of {x} is {x**y}")
        else:
            print("Error: Cannot compute square root of a negative number.")
    case _:
        print("Invalid operation. Please enter add, sub, mul, div, or sqrt.")
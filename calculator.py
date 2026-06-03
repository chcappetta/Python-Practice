def modulo(x,y):
    return x%y

def division(x,y):
    return x/y

def multiplication(x,y):
    return x*y

def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def calculator_script():
    print("Welcome to Simple Calculator. Enter Exit to return.")
    while True:
        print()
        func = input(f"Choose a function: +,-,*,/,% : ")
        if func.lower() == "exit":
            print()
            print("Exiting Calculator...")
            print()
            break
        if func == "+":
            num1 = input("What is your first number? ")
            num2 = input("And the second? ")
            print()
            print(f"{num1} + {num2} = {addition(int(num1),int(num2))}")
            continue
        if func == "-":
            num1 = input("What is your first number? ")
            num2 = input("And the second? ")
            print()
            print(f"{num1} - {num2} = {subtraction(int(num1),int(num2))}")
            continue
        if func == "*":
            num1 = input("What is your first number? ")
            num2 = input("And the second? ")
            print()
            print(f"{num1} * {num2} = {multiplication(int(num1),int(num2))}")
            continue
        if func == "/":
            num1 = input("What is your first number? ")
            num2 = input("And the second? ")
            print()
            print(f"{num1} / {num2} = {division(int(num1),int(num2))}")
            continue
        if func == "%":
            num1 = input("What is your first number? ")
            num2 = input("And the second? ")
            print()
            print(f"{num1} % {num2} = {modulo(int(num1),int(num2))}")
            continue

import calc_logo

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

operations = {
    '+': add,
    '-': subtract, 
    '*': multiply, 
    '/': divide,
}

should_continue = 'n'

print(calc_logo.logo)
print("\n" * 3)

while 0 < 1: 
    type = ""
    if should_continue == 'n':
        original_number = float(input("What is the first number?:\n"))

    while type not in ["+","-","*","/"]:
        type = input("\n\n\n+\n-\n*\n/\nPick an operation:\n")
        
    next_number = float(input("What's the next number?:\n"))

    if type == "+":
        answer = add(original_number, next_number)
        print (f"{original_number} + {next_number} = {answer}")
    elif type == "-":
        answer = subtract(original_number, next_number)
        print (f"{original_number} - {next_number} = {answer}")     
    elif type == "*":
        answer = multiply(original_number, next_number)
        print (f"{original_number} * {next_number} = {answer}") 
    elif type == "/":
        answer = divide(original_number, next_number) 
        print (f"{original_number} / {next_number} = {answer}")

    should_continue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'x' to close the calculator:\n").lower()
    print(original_number)
    if should_continue == "y":
        original_number = answer
        print (original_number)
    elif should_continue == "n":
        original_number = 0

    elif should_continue == "x":
        break


    



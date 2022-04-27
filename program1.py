def add (a,b):
    return a + b

def sub (a,b):
    return a - b

def mul (a,b):
    return a * b

def div (a,b):
    return a / b

a = float(input())
b = float(input())

type_of_operation = input()

if type_of_operation == "add":
    print(add(a,b))

elif type_of_operation == "sub":
    print(sub(a,b))

elif type_of_operation == "mul":
    print(mul(a,b))

elif type_of_operation == "div":
    print(div(a,b))

else:
    print("invalid operation")

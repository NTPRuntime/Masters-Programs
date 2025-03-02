import math

print("-------------Welcome to a simple calculator-------------")
first_num = int(input("What is the first number?: "))
second_num = int(input("What is the second number?: "))
operator = input("What is the operator? +, -, *, /, MOD, ^: ")
result = None
if operator == "+":
    result = first_num + second_num
elif operator == "-":
    result = first_num - second_num
elif operator == "*":
    result = first_num * second_num
elif operator == "/":
    result = first_num / second_num
elif operator == "MOD":
    result = first_num % second_num
elif operator == "^":
    result = first_num ^ second_num
else:
    print("Unknown Operator")

if result != None:
    print(f"The result is: {result}")
else:
    print("Exiting....")

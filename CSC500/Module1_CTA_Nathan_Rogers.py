
def part_1():
    print("Part 1: Addition and Subtraction")
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number Number: "))
    print(f"Addition Result: {num1+num2}")
    print(f"Subtraction Result: {num1-num2}")

def part_2():
    print("Part 2: Multiplication and Division")
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    print(f"Multiplication Result: {num1*num2}")
    if num2 > 0 or num2 < 0:
        print(f"Division Result: {num1/num2}")
    elif num2 == 0:
        print("Divide by 0 Error")
    
if __name__ == "__main__":
    part_1()
    part_2()
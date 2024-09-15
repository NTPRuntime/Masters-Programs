
def part1():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    num_years = int(input("Number of Years: "))
    total_months = 0
    total_rainfall = 0
    for i in range(num_years):
        for j in range(12):
            monthly_rainfall = float(input(f"What was {months[j]}'s rainfall in year {i+1} (inches)? "))
            total_months += 1
            total_rainfall += monthly_rainfall
        
    print(f"Total Months: {total_months} or {num_years} year(s)")
    print(f"Total Inches of Rainfall: {total_rainfall}")
    print(f"Average Rainfall Per Month: {total_rainfall/total_months}")

def part2():
    point_map = {
        "0": 0,
        "2": 5,
        "4": 15,
        "6": 30,
        "8": 60
    }
    purchased_books = input("How many books have you purchased this month? ")
    if int(purchased_books) > 8:
        print("Total Points Awarded This Month: 60")
    else:
        print(f"Total Points Awarded This Month: {point_map[purchased_books]}")

def main():
    print("------Part 1------")
    part1()
    print("------Part 2------")
    part2()

if __name__ == "__main__":
    main()
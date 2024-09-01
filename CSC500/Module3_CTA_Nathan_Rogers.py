def part_1():
    meal_total = float(input("What is the meal total? "))
    print("After Sales tax: 7%, and Tip: 18%")
    print(f"Final Total: {"{:.2f}".format(meal_total + (meal_total * 0.07) + (meal_total * 0.18))}")

def part_2():
    time_now = int(input("What is the current hour (24h time)? "))
    alarm_time = int(input("How many hours do you wish to set an alarm for? "))
    military_time = (time_now + alarm_time) % 24
    print(f"Your alarm will go off at {military_time}")
    
if __name__ == "__main__":
    part_1()
    part_2()
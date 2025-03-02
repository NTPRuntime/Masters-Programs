
location_dict = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411,
}

instructor_dict = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

time_dict = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.",
}

def main():
    while True:
        course_input = str(input("Course Number: "))
        try:
            print(f"{course_input} is in room {location_dict[course_input]} at {time_dict[course_input]} taught by Professor {instructor_dict[course_input]}")
            break
        except:
            print("Enter a new course number....That course number doesnt exist.")

if __name__ == "__main__":
    main()
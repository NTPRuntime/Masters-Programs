
class Friend:

    def __init__(self, name, age, relation):
        self.name = name
        self.age = age
        self.relation = relation
        self.__secret = "they are dating Shelby"

    def ask_for_secret(self):
        print(f"{self.name}'s secret is {self.__secret}")

    def remember_details(self):
        print(f"My friend {self.name} is {self.age} years old and is my {self.relation}")

Mike = Friend("Mike", 18, "Best Friend")
Mike.remember_details()
Mike.ask_for_secret()

try:
    print(Mike.__secret)
except:
    print("Cannot read Mike's Mind")

class CheckWriter:

    def __init__(self, amount):
        self.dollars, self.cents = self.split_amount(amount)
        self.write_check()

    def validate_amount(self):
        try:
            if self.dollars < 0 or self.cents < 0 or self.cents > 99:
                raise ValueError("Amount must be positive.")
            return True
        except ValueError:
            print("Invalid input. Please enter a valid dollar and cents amount.")
            return False

    def split_amount(self, amount):
        dollars = int(amount.split(".")[0])
        cents = int(amount.split(".")[1])
        return dollars, cents

    def convert_number_to_words(self, number):
        ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        thousands = ["", "thousand", "million", "billion"]

        if number == 0:
            return "zero"
        
        if number < 10:
            return ones[number]
        elif 10 < number < 20:
            return teens[number - 11]
        elif number < 100:
            return tens[number // 10] + (" " + ones[number % 10] if number % 10 != 0 else "")
        elif number < 1000:
            return ones[number // 100] + " hundred" + (" " + self.convert_number_to_words(number % 100) if number % 100 != 0 else "")
        
        for i, unit in enumerate(thousands):
            if number < 1000 ** (i + 1):
                return self.convert_number_to_words(number // (1000 ** i)) + " " + unit + (" " + self.convert_number_to_words(number % (1000 ** i)) if number % (1000 ** i) != 0 else "")

        return "Number too large!"

    def format_words(self, dollars_in_words, cents_in_words):
        return f"{dollars_in_words} and {cents_in_words}/100"

    def convert_dollars_to_words(self):
        if self.dollars == 0:
            return "zero dollars"
        
        words = self.convert_number_to_words(self.dollars)
        return f"{words} dollars"

    def convert_cents_to_words(self):
        if self.cents == 0:
            return "00"
        
        return f"{self.cents:02d}"

    def write_check(self):
        if self.validate_amount():
            dollars_in_words = self.convert_dollars_to_words()
            cents_in_words = self.convert_cents_to_words()
            check_text = self.format_words(dollars_in_words, cents_in_words)
            print(check_text)  # Output: "one thousand two hundred thirty-four dollars and 56/100"

# Test Case
amount_input = str(float(input("Input an amount to convert: ")))
check_writer = CheckWriter(amount_input)


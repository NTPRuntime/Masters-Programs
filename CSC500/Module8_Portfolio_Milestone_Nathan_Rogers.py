from datetime import datetime

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
class ItemToPurchase:
    def __init__(self, name:str="none", price:float=0.0, item_quantity:int=0, item_description:str=''):
        self.name = name
        self.price = price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(f"{self.name} {self.item_quantity} @ ${self.price:.2f} = ${(self.item_quantity * self.price):.2f}")

class ShoppingCart:
    def __init__(self, customer_name:str=None, current_date:str="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
        self.total = 0.0

    def add_item(self):
        item_name = str(input("Enter the item name: "))
        item_price = float(input("Enter the item price: $"))
        item_quantity = int(input("Enter the item quantity: "))
        item_description = str(input("Enter the items description: "))
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart")

    def modify_item(self, item_name):
        for item in self.cart_items:
            if item.name == item_name:
                while True:
                    modify_param = str(input("What would you like to modify?\nq - Item Quantity\nd - Item Description\np - Items Price\ne - Exit\n-> "))
                    if modify_param == "q":
                        new_quantity = int(input(f"Enter a new quantity for {item.name}: "))
                        item.item_quantity = new_quantity
                    if modify_param == 'd':
                        new_description = str(input(f"Enter a new description for {item.name}: "))
                        item.item_description = new_description
                    if modify_param == 'p':
                        new_price = float(input(f"Enter a new price for {item.name}: $"))
                        item.price = new_price
                    if modify_param == "e":
                        return
        print("Item not found in cart")

    def get_num_items_in_cart(self):
        quantity_total = 0
        for item in self.cart_items:
            quantity_total += item.item_quantity
        return quantity_total

    def get_cost_of_cart(self):
        self.total = 0
        for item in self.cart_items:
            self.total += (item.price * item.item_quantity)
        return self.total

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if len(self.cart_items) > 0:
            for item in self.cart_items:
                item.print_item_cost()
        else:
            print("SHOPPING CART IS EMPTY")
        print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.item_description}")

def print_menu():
    new_cart = str(input("Start a new cart? (y/n) "))
    if new_cart == "y":
        customer_name = str(input("What is your name? "))
        current_date = f"{months[datetime.now().month - 1]} {datetime.now().day}, {datetime.now().year}"
        shopping_cart = ShoppingCart(customer_name, current_date)
        while True:
            print("---------MENU---------")
            print("a - Add item to cart")
            print("r - Remove item to cart")
            print("c - Modify Item")
            print("i - Output items' description")
            print("o - Output shopping cart")
            print("q - Quit")
            choice = str(input("Choose an Option: "))
            if choice == "a":
                shopping_cart.add_item()
            elif choice == "r":
                remove_item = str(input("Which item would you like to remove? "))
                shopping_cart.remove_item(remove_item)
            elif choice == "c":
                modify_item_selection = str(input("Which item would you like to change? "))
                shopping_cart.modify_item(modify_item_selection)
            elif choice == "i":
                shopping_cart.print_descriptions()
            elif choice == "o":
                shopping_cart.print_total()
            elif choice == "q":
                break
            else:
                print("Choose an option from above.")

    if new_cart == 'n':
        print("Exiting....")
        
if __name__ == "__main__":
    print_menu()
    
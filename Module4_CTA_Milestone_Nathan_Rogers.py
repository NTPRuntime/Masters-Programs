class ItemToPurchase:
    def __init__(self, name:str="none", price:float=0.0, item_quantity:int=0):
        self.name = name
        self.price = price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.name} {self.item_quantity} @ ${self.price} = ${self.item_quantity * self.price}")

def main():
    purchase_list = []
    total_price = 0
    items = int(input("How many items to purchase? "))
    for item in range(items):
        print(f"Item {item+1}")
        item_name = str(input("Enter the item name: "))
        item_price = float(input("Enter the item price: $"))
        item_quantity = int(input("Enter the item quantity: "))
        total_price += (item_price * item_quantity)
        purchase_list.append(ItemToPurchase(item_name, item_price, item_quantity))

    print("TOTAL COST")
    for purchased_item in purchase_list:
        purchased_item.print_item_cost()
    print(f"Total: ${total_price}")

if __name__ == "__main__":
    main()
    
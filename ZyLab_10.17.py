"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

ZyLab - 10.17
"""
class ItemToPurchase:

    def __init__(self, item_name="none", item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $"
        + str( self.item_price * self.item_quantity ))

if __name__ == "__main__":

    item = ItemToPurchase()
    print("Item 1")

    item.item_name = input("Enter the item name:\n")
    item.item_price = int(input("Enter the item price:\n"))
    item.item_quantity = int(input("Enter the item quantity:\n"))

    print()

    another_item = ItemToPurchase()
    print("Item 2")

    another_item.item_name = input("Enter the item name:\n")
    another_item.item_price = int(input("Enter the item price:\n"))
    another_item.item_quantity = int(input("Enter the item quantity:\n"))


    print()

    print("TOTAL COST")
    item.print_item_cost()
    another_item.print_item_cost()

    total1 = int(item.item_price * item.item_quantity)
    total2 = int(another_item.item_price * another_item.item_quantity)

    sum = total1 + total2
    print()
    print("Total: $" + str(int(sum)))
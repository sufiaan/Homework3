"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

ZyLab - 10.19
"""


class ItemToPurchase:

    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print((self.item_name, self.item_quantity + "@ $" + self.item_price + "= $" +
               self.item_price * self.item_quantity))

    def print_item_description(self):
        print(self.item_name, ": ", self.item_description, "\n")


class ShoppingCart:

    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self):
        print('ADD ITEM TO CART')
        item_name = str(input('Enter the item name:\n'))
        item_description = str(input('Enter the item description:\n'))
        item_price = int(input('Enter the item price:\n'))
        item_quantity = int(input('Enter the item quantity:\n'))
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    def remove_item(self):
        print('REMOVE ITEM FROM CART')

        string = str(input('Enter name of item to remove:'))
        print()
        i = 0

        for item in self.cart_items:
            if (item.item_name == string):
                del self.cart_items[i]
                flag = True
                break

            else:
                flag = False
            i += 1

        if (flag == False):
            print('Item not found in cart. Nothing removed.')

    def modify_item(self):
        print('CHANGE ITEM QUANTITY')

        name = str(input('Enter the item name:'))
        print()

        for item in self.cart_items:
            if (item.item_name == name):
                quantity = int(input('Enter the new quantity:'))
                print()
                item.item_quantity = quantity
                flag = True
                break

            else:
                flag = False

        if not flag:
            print('Item not found in cart. Nothing modified.')
        print()

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0

        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost

        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            self.output_cart()

    def print_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)

        print('\nItem Descriptions')

        for item in self.cart_items:
            print(item.item_name + ": " + item.item_description)

    def output_cart(self):
        print('OUTPUT SHOPPING CART')
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)

        print('Number of Items:', self.get_num_items_in_cart())

        print()

        total = 0
        for item in self.cart_items:
            print('{} {} @ ${} = ${}'.format(item.item_name, item.item_quantity,
                                             item.item_price, (item.item_price * item.item_quantity)))
            total = total + (item.item_price * item.item_quantity)

        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        print()

        print("Total: $" + str(total))


def print_menu(customer_Cart):
    menu = (
        '\nMENU\n' 'a - Add item to cart\n' 'r - Remove item from cart\n' 'c - Change item quantity\n'
        'i - Output items\' descriptions\n' 'o - Output shopping cart\n' 'q - Quit\n')

    choice = ''
    while (choice != 'q'):
        print(menu)
        choice = input('Choose an option:\n')

        while choice != 'a' and choice != 'o' and choice != 'i' and choice != 'r' and choice != 'c' and choice != 'q': choice = input(
            'Choose an option:\n')

        if (choice == 'a'):
            customer_Cart.add_item()

        if (choice == 'o'):
            customer_Cart.output_cart()

        if (choice == 'i'):
            customer_Cart.print_descriptions()

        if (choice == 'r'):
            customer_Cart.remove_item()

        if (choice == 'c'):
            customer_Cart.modify_item()


customer_name = str(input('Enter customer\'s name:\n'))
current_date = str(input('Enter today\'s date:\n'))
print()

print('Customer name:', customer_name, end='\n')
print('Today\'s date:', current_date)

print_menu(ShoppingCart(customer_name, current_date))

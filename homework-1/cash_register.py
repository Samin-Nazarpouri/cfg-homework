"""

TASK 1

Write a class to represent a Cash Register.
Your class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self, discount):
        self.total_items = dict() # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):
        self.total_items[item] = price
        return self.total_items

    def remove_item(self, item):
        self.total_items.pop(item)
        return self.total_items

    def apply_discount(self, percentage):
        return self.total_price - (self.total_price * (percentage/100))


    def get_total(self):
        self.total_price = sum(float(self.total_items[item]) for item in self.total_items)
        return self.total_price

    def show_items(self):
        for item in self.total_items:
            print(item)

    def reset_register(self):
        self.total_items.clear()


# EXAMPLE code run:

groceries = CashRegister(discount=0.5)

#ADD example:
groceries.add_item('apple', '2.25')
groceries.add_item('banana', '5.00')
groceries.add_item('orange', '3.45')
groceries.add_item('peach', '3.50')
groceries.add_item('celery', '2.50')

#Remove example:
groceries.remove_item('apple')

# #Get total example:
print(groceries.get_total())

#Applying discount:
total_price_before_discount= print(groceries.get_total())
print(groceries.apply_discount(50))

# #Show items:
groceries.show_items()

#Reset register:
groceries.reset_register()
groceries.show_items()
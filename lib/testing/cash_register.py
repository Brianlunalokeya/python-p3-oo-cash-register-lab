#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)


    def apply_discount(self):
         if self.discount == 0:
            print("There is no discount to apply.")
         else:
            self.total -= self.total * (self.discount / 100)
            print("After the discount, the total comes to ${:.2f}.".format(self.total))


    def void_last_transaction(self):
        if self.items:
            last_item_price = float(self.items.pop())
            self.total -= last_item_price
        else:
            print("No transactions to void.")


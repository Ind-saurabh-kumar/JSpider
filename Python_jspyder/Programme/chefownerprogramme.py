# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 00:22:41 2024

@author: saura
"""

class Owner:
    def __init__(self, name):
        self.name = name

    def request_menu(self, chef):
        print(f"{self.name} requests the menu.")
        chef.provide_menu()

    def select_dish(self, chef, dish):
        print(f"{self.name} selects the dish: {dish}")
        chef.get_groceries(dish)


class Chef:
    def __init__(self, name):
        self.name = name
        self.menu = ["Pizza", "Pasta"]

    def provide_menu(self):
        print(f"{self.name} provides the menu: {', '.join(self.menu)}")

    def get_groceries(self, dish):
        print(f"{self.name} goes to the shop to get groceries for {dish}.")
        shopkeeper = Shopkeeper("John")
        groceries = shopkeeper.sell_groceries(dish)
        self.prepare_dish(dish, groceries)

    def prepare_dish(self, dish, groceries):
        print(f"{self.name} prepares the dish: {dish} with {', '.join(groceries)}.")
        print(f"{self.name} serves the dish: {dish}.")


class Shopkeeper:
    def __init__(self, name):
        self.name = name

    def sell_groceries(self, dish):
        grocery_list = {
            "Pizza": ["dough", "cheese", "tomato sauce", "pepperoni"],
            "Pasta": ["pasta", "tomato sauce", "cheese"],   
        }
        groceries = grocery_list.get(dish, [])
        print(f"{self.name} sells groceries: {', '.join(groceries)} for {dish}.")
        self.receive_payment()
        return groceries

    def receive_payment(self):
        print(f"{self.name} receives payment for the groceries.")


# Simulate the interaction
owner = Owner("Saurabh")
chef = Chef("Kumar")

owner.request_menu(chef)
owner.select_dish(chef, "Pizza")

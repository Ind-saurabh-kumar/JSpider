def request_menu():
    menu = ["Pizza", "Pasta", "Salad", "Burger"]
    print("Menu:", ", ".join(menu))
    return menu

def select_dish(menu):
    dish = input("Select a dish from the menu: ")
    if dish in menu:
        return dish
    else:
        print("Dish not available. Please select again.")
        return select_dish(menu)

def get_groceries(dish):
    grocery_list = {
        "Pizza": ["dough", "cheese", "tomato sauce", "pepperoni"],
        "Pasta": ["pasta", "tomato sauce", "cheese"],
        "Salad": ["lettuce", "tomato", "cucumber", "dressing"],
        "Burger": ["bun", "beef patty", "cheese", "lettuce", "tomato"]
    }
    groceries = grocery_list.get(dish, [])
    if groceries:
        print(f"Purchasing groceries for {dish}: {', '.join(groceries)}")
        receive_payment()
        return groceries
    else:
        print("No groceries needed.")
        return []

def receive_payment():
    print("Payment received for groceries.")

def prepare_dish(dish, groceries):
    if groceries:
        print(f"Preparing the dish: {dish} with {', '.join(groceries)}.")
        print(f"Dish {dish} is ready and served.")
    else:
        print(f"Preparing the dish: {dish}.")

# Simulate the interaction
menu = request_menu()
selected_dish = select_dish(menu)
groceries = get_groceries(selected_dish)
prepare_dish(selected_dish, groceries)

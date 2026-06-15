# Exercise 14: Concession Stand Program

menu = {"pizza": 20.00,
               "nachos": 30.50,
               "popcorn": 15.00,
               "fries": 20.50,
               "chips": 20.00,
               "pretzel": 15.50,
               "soda": 20.00,
               "lemonade": 10.25}
cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ₱{value:.2f}")
print("------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------ YOUR ORDER ------")
for food in cart:
    total += menu.get(food)
    print(food)

print()
print(f"Total is: ₱{total:.2f}")

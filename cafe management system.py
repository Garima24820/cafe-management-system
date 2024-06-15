#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Pragya priya
#
# Created:     16-06-2024
# Copyright:   (c) Pragya priya 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Cafe Management System

# Menu dictionary containing item names as keys and their prices as values
menu = {
    "coffee": 3.50,
    "tea": 2.00,
    "sandwich": 5.00,
    "cake": 3.75,
    "salad": 6.25
}

# Function to display the menu
def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

# Function to take customer's order
def take_order():
    order = {}
    while True:
        display_menu()
        item = input("Enter item (or 'done' to finish): ").strip().lower()
        if item == 'done':
            break
        elif item in menu:
            try:
                quantity = int(input(f"Enter quantity for {item}: "))
                if quantity > 0:
                    order[item] = order.get(item, 0) + quantity
                else:
                    print("Invalid quantity. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Item not found in menu. Please choose again.")
    return order

# Function to calculate the total bill
def calculate_bill(order):
    total = 0.0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total

# Main function to run the cafe management system
def main():
    print("Welcome to the Cafe Management System!")
    print("====================================")
    while True:
        print("\nOptions:")
        print("1. Take Order")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == '1':
            order = take_order()
            total_bill = calculate_bill(order)
            print("\nOrder Summary:")
            for item, quantity in order.items():
                print(f"{item}: {quantity}")
            print(f"Total Bill: ${total_bill:.2f}")
        elif choice == '2':
            print("Exiting the Cafe Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

print("BENITAH'S HOTEL")
def menu():
    print("Breakfast")
    print("Lunch")
MENU = {
      "Breakfast": {
            1: "Coffee with eggs benedict, UGX 40,000",
            2: "African tea with avocado toast, UGX 35,000",
            3: "Juice with pancakes, UGX 25,000",
            4: "Breakfast Burrito, UGX 40,000"
        },
        "Lunch": {
            1: "Grilled chicken with chips, UGX 50,000",
            2: "Pasta and steak, UGX 45,000",
            3: "Chicken noodles, UGX 35,000",
            4: "Matooke and pasted g.nuts, UGX 15,000"
        }
  }
print("Breakfast Menu:")
for item, price in MENU["Breakfast"].items():
    print(f"{item}. {price}")
print("Lunch Menu:")
for item, price in MENU["Lunch"].items():
    print(f"{item}. {price}")
def get_choice(menu_type):
    while True:
        choice = int(input(f"Please enter your choice for {menu_type} (1-{len(MENU[menu_type])}): "))
        if choice in (MENU[menu_type]):
            return choice
        else:
          print(f"Invalid choice. Please choose a number between 1 and {len(MENU[menu_type])}.")
def main():
    while True:
       print("WELCOME TO BENITAH'S HOTEL!")
       print("1.Breakfast")
       print("2.Lunch")
       print("3.Exit")
       try:
           choice_value = int(input("Please enter your choice (1 for Breakfast, 2 for Lunch): "))
           if choice_value == 1:
            breakfast_choice = get_choice("Breakfast")
            print(f"You have chosen: {MENU['Breakfast'][breakfast_choice]}")
           elif choice_value == 2:
            lunch_choice = get_choice("Lunch")
            print(f"You have chosen: {MENU['Lunch'][lunch_choice]}")
           elif choice_value == 3:
            print("Thank you for visiting Benitah's Hotel! Goodbye!")
           else:
            print("Invalid choice, please choose valid option,Thank you")
       except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
if __name__ == "__main__":
        main()
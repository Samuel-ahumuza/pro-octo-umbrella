balance = 0.0
while True:
    try:
        savings = input("Enter an amount to add to your savings (or 'done' to finish): ")
        if savings.lower() == 'done':
            break
        savings = float(savings)
        if savings >= 0:
            balance += savings
            print(f"Added UGX{savings:.2f}. Current balance is: UGX{balance:.2f}")
        else:
            print("Please enter a positive number.")

    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")
        print("\n---")
print(f"Final savings balance: UGX{balance:.2f}")



try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    total = value/total_value * 100
    print(f"That is {total}%")
except SyntaxError:
    print("You need to enter a number. Run the program again.")
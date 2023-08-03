total_value = float(input("Enter total value: "))
value = float(input("Enter value: "))
total = value/total_value * 100
print(f"That is {total}%")
if total_value == 0:
    exit("Your total value cannot be zero")
height = int(input("Enter your height in inches: "))

if height > 3:
    print(f"Token required due to your height {height}, more than 3.")
else:
    print("No token required")

print("________________________________________")
age = int(input("Enter your age in years: "))
if age >= 18:
     print("You are eligible for vote")
else:
    print("You are not eligible for vote")
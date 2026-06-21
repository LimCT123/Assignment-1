name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Print greeting
print(f"Hello {name}, welcome to RISC-V training!")

# Print age next year
print(f"Next year you will be {age + 1} years old.")

# Print Day 1 to Day 5
for day in range(1, 6):
    print(f"Day {day}")

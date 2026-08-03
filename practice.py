# check largest_number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)

#  check positive_negative
num = int(input("Enter a number: "))
if num >= 0:
    print("Positive Number")
else:
    print("Negative Number")

# check even_odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# voting_checker
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible")
else:
    print("Not eligible")
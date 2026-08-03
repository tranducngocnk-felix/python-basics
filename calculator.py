first_number = int(input("Which first number do you want to calculate? "))
second_number = int(input("Which second number do you want to calculate? "))
print("The sum of", first_number, "and", second_number, "is", first_number + second_number)
print("The difference of", first_number, "and", second_number, "is", first_number - second_number)
print("The product of", first_number, "and", second_number, "is", first_number * second_number)
if second_number == 0:
    print("Cannot divide by zero.")
else:
    print("the quotient of", first_number, "and", second_number, "is", first_number / second_number)

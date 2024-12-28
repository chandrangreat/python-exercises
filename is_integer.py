num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
print(f"""The difference between {num_1} and {num_2} is an integer? {(num_1 - num_2).is_integer()}!""")
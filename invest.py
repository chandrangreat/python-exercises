def invest(amount, rate, years):
    for num in range(years):
        amount = amount + (amount * (rate/100))
        print(f"year {num + 1}: ${amount:.2f}")
    return amount

initial_amount = float(input("Enter the initial amount "))
rate_of_interest_in_percentage = float(input("Enter the rate of interest in percentages "))
number_of_years = int(input("Enter the number of years "))
invest(initial_amount, rate_of_interest_in_percentage, number_of_years)
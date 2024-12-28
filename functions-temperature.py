def convert_cel_to_far(temp_cel):
    """Converts temperature temp_cell in Celcuis to Fahrenheit"""
    temp_far = float((temp_cel * 9/5) + 32)
    return temp_far

def convert_far_to_cel(temp_far):
    """Converts temperature temp_far in Fahrenheit to Celcuis"""
    temp_cel = float((temp_far - 32) * 5/9)
    return temp_cel

get_temp_in_cel = float(input("Enter temperature in Celcius "))
print(f"Temperature in Fahrenheit is {convert_cel_to_far(get_temp_in_cel):.2f} degrees Fahrenheit")
get_temp_in_far = float(input("Enter temperature in Fahrenheit "))
print(f"Temperature in Celcius is {convert_far_to_cel(get_temp_in_far):.2f} degrees Celcuis")
    
def convert_to_upper_if_needed(input_string):
    if len(input_string) < 4:
        if input_string.isupper():
            return input_string.upper()
        else:
            return input_string

    first_four = input_string[:4]
    upper_count = sum(1 for char in first_four if char.isupper())
    
    if upper_count >= 3:
        return input_string.upper()
    else:
        return input_string

input_string = input("Введите строку: ")
output_string = convert_to_upper_if_needed(input_string)
print(output_string)

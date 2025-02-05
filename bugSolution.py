def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if all(x == 0 for x in numbers):
        return 0 #Handle list with all zeros
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [1, 2, 3, 4, 5]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}")

my_list_with_zero = [1,0,2,0,3]
result = calculate_average(my_list_with_zero)
print(f"The average is: {result}")

my_list_all_zeros = [0,0,0]
result = calculate_average(my_list_all_zeros)
print(f"The average is: {result}") #This will output 0 which is correct
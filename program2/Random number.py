import sys
import json
import random

if len(sys.argv) != 7:
    print("Please provide 6 consecutive numbers as command line arguments.")
    sys.exit(1)

numbers = [int(arg) for arg in sys.argv[1:]]

def perform_subtraction(numbers):
    result = [str(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1)]
    print("Subtraction result:", ", ".join(result))

def perform_multiplication(numbers):
    multiplication_result = 1
    for num in numbers:
        multiplication_result *= num

    output_json = {f"InputNumber{i+1}": num for i, num in enumerate(numbers)}
    output_json["Multiplication"] = multiplication_result

    with open("multiplication_result.json", "w") as json_file:
        json.dump(output_json, json_file)

def pick_random_number(numbers):
    random_num = random.choice(numbers)
    print("Randomly picked number:", random_num)

def print_sorted_numbers(numbers, reverse=False):
    sorted_numbers = sorted(numbers, reverse=reverse)
    print("Sorted numbers ({}):".format("highest to lowest" if reverse else "lowest to highest"), sorted_numbers)

# User menu
menu = """
Menu:
1. Perform subtraction
2. Perform multiplication
3. Pick a random number
4. Print sorted (highest to lowest) numbers
5. Print sorted (lowest to highest) numbers
Input your choice (1-5): 
"""

choice = input(menu)

if choice == '1':
    perform_subtraction(numbers)
elif choice == '2':
    perform_multiplication(numbers)
    print("Multiplication result stored in 'multiplication_result.json'")
elif choice == '3':
    pick_random_number(numbers)
elif choice == '4':
    print_sorted_numbers(numbers, reverse=True)
elif choice == '5':
    print_sorted_numbers(numbers)
else:
    print("Invalid choice. Please input a number from 1 to 5.")


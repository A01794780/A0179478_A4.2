"""Comvert a the numbers is a file to binary and hexadecimal"""
import sys
import time

def to_binary(n):
    """Convert number to binary"""
    binary = ""
    if n == 0:
        return "0"
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def to_hexadecimal(n):
    """Convert number to hexadecimal"""
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    if n == 0:
        return "0"
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n = n // 16
    return hexadecimal

def convert_numbers(file_path):
    """Convert the numnbers in a file to binary and hexadecimal"""
    start_time = time.time()

    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return

    results = []

    for line in lines:
        line = line.strip()
        try:
            number = int(line)
            binary = to_binary(number)
            hexadecimal = to_hexadecimal(number)
            result = f"Number: {number} = Binary: {binary}, Hexadecimal: {hexadecimal}"
            results.append(result)
            print(result)
        except ValueError:
            error_message = f"Invalid data: {line} is not a valid number."
            results.append(error_message)
            print(error_message)

    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_message = f"Time elapsed: {elapsed_time:.2f} seconds"
    results.append(elapsed_time_message)
    print(elapsed_time_message)

    with open("ConvertionResults.txt", 'w', encoding="utf-8") as result_file:
        for result in results:
            result_file.write(result + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
    else:
        convert_numbers(sys.argv[1])

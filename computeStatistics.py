"""Compute statistics for the content in a file"""
import sys
import time

def read_numbers_from_file(file_name):
    """Read the numbers contained in a file"""
    numbers = []
    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Invalid data found and skipped: {line.strip()}")
    return numbers

def calculate_mean(numbers):
    """Calculate the mean"""
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """Calculate the median"""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    """Calculate the mode"""
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    max_count = max(frequency.values())
    modes = [number for number, count in frequency.items() if count == max_count]
    return modes

def calculate_variance(numbers, mean):
    """Calculate the variance"""
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(variance):
    """Calculate the standard deviation"""
    return variance ** 0.5

def write_statistics_to_file(file_name, statistics, elapsed_time):
    """Write the statistics calclated to a file"""
    with open(file_name, 'w', encoding="utf-8") as file:
        for key, value in statistics.items():
            file.write(f"{key}: {value}\n")
        file.write(f"Time elapsed: {elapsed_time} seconds\n")

def main():
    """Main point to execute the program"""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]

    start_time = time.time()

    numbers = read_numbers_from_file(input_file)

    if not numbers:
        print("No valid data to process.")
        sys.exit(1)

    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    standard_deviation = calculate_standard_deviation(variance)

    elapsed_time = time.time() - start_time

    statistics = {
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Variance": variance,
        "Standard Deviation": standard_deviation
    }

    for key, value in statistics.items():
        print(f"{key}: {value}")

    print(f"Time elapsed: {elapsed_time} seconds")

    write_statistics_to_file("StatisticsResults.txt", statistics, elapsed_time)

if __name__ == "__main__":
    main()

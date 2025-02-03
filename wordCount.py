"""Count the number of times a word is wrriten in a file"""
import sys
import time

def count_words(file_path):
    """Count the words"""
    word_count = {}
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.lower().strip('.,!?\";:()[]{}')
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    except OSError as e:
        print(f"Error reading file: {e}")

    return word_count

def write_results(word_count, elapsed_time):
    """Write the words count results to a file"""
    try:
        with open('WordCountResults.txt', 'w', encoding="utf-8") as result_file:
            for word, count in word_count.items():
                result_file.write(f"{word}: {count}\n")
            result_file.write(f"\nTime elapsed: {elapsed_time:.2f} seconds\n")
    except OSError as e:
        print(f"Error writing results: {e}")

def main():
    """Main point to execute the program"""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        return

    file_path = sys.argv[1]

    start_time = time.time()

    word_count = count_words(file_path)

    elapsed_time = time.time() - start_time

    for word, count in word_count.items():
        print(f"{word}: {count}")

    print(f"\nTime elapsed: {elapsed_time:.2f} seconds")

    write_results(word_count, elapsed_time)

if __name__ == "__main__":
    main()

from stats import (count_words, count_characters, chars_dict_to_sorted_list)
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]


def main():
    text = get_book_text(book_path)
    num_words = count_words(text)
    character_dict = count_characters(text)
    listOfSorted = chars_dict_to_sorted_list(character_dict)
    print(f"Found {num_words} total words")
    print(listOfSorted)

def print_report(book_path, num_words, listOfSorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for character in listOfSorted:
        if not character.isalpha():
            print(f"{character}: {count_characters}")

    print("============= END ===============") 

main()
from stats import count_words, count_characters, chars_dict_to_sorted_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(book_path)
    num_words = count_words(text)
    character_dict = count_characters(text)
    listOfSorted = chars_dict_to_sorted_list(character_dict)
    print_report(book_path, num_words, listOfSorted)

def print_report(book_path, num_words, listOfSorted):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for first, second in listOfSorted:
        if first.isalpha():
            print(f"{first}: {second}")

    print("============= END ===============")   
    


main()
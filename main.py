from stats import count_words
from stats import count_characters
from stats import sort_characters
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    sorted_chars = sort_characters(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at"+ sys.argv[1]+"...")
    print("----------- WORD COUNT ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char['char']}: {char['count']}")
    print("============== END ==============")



main()
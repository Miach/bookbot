from stats import count_words
from stats import count_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    count_words(file_contents)
    count_characters(file_contents)


main()
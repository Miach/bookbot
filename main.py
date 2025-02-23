def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    words = file_contents.split()
    word_length = len(words)
    print(f"{word_length} words found in the document")

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    count_words(file_contents)

main()
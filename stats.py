
def count_words(file_contents):
    words = file_contents.split()
    word_length = len(words)
    print(f"{word_length} words found in the document")

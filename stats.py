
def count_words(file_contents):
    words = file_contents.split()
    word_length = len(words)
    print(f"{word_length} words found in the document")

def count_characters(file_contents):
    file_contents = file_contents.lower()
    unique_characters = {}
    for char in file_contents:
        if char in unique_characters:
            unique_characters[char] += 1
        else:
            unique_characters[char] = 1
    print(unique_characters)

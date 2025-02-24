
def count_words(file_contents):
    words = file_contents.split()
    word_length = len(words)
    return word_length

def count_characters(file_contents):
    file_contents = file_contents.lower()
    unique_characters = {}
    for char in file_contents:
        if char in unique_characters:
            unique_characters[char] += 1
        else:
            unique_characters[char] = 1
    return unique_characters

def sort_characters(unique_characters):
    sorted_characters = []
    for char in unique_characters:
        if char.isalpha():
            sorted_characters.append({"char": char, "count": unique_characters[char]})
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters

def sort_on(unique_characters):
    return unique_characters["count"]

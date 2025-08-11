def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text:
        lowercase_char = char.lower()
        char_count[lowercase_char] = char_count.get(lowercase_char, 0) + 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_character_count(char_count):
    sorted_count = []
    for key, value in char_count.items():
        char_dict = {"char": key, "num": value}
        sorted_count.append(char_dict)
    sorted_count.sort(key=sort_on, reverse=True)
    return sorted_count
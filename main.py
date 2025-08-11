from stats import count_words
from stats import count_characters
from stats import sort_character_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    filepath = "books/frankenstein.txt"
    book_contents = get_book_text(filepath)
    word_count = count_words(book_contents)
    char_count = count_characters(book_contents)
    sorted_count = sort_character_count(char_count)
    print(f"{word_count} words found in the document")
    print(char_count)
    print(sorted_count)

main()





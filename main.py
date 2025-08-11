import sys
from stats import count_words
from stats import count_characters
from stats import sort_character_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    filepath = sys.argv[1]
    book_contents = get_book_text(filepath)
    word_count = count_words(book_contents)
    char_count = count_characters(book_contents)
    sorted_count = sort_character_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for entry in sorted_count:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")


main()
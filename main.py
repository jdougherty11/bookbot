from stats import count_words


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    filepath = "books/frankenstein.txt"
    book_contents = get_book_text(filepath)
    word_count = count_words(book_contents)
    print(f"{word_count} words found in the document")

main()





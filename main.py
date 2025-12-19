from stats import get_num_words, get_character_counts, get_sorted_dictionary


def get_book_text(filepath: str):
    file_contents = ""

    with open(filepath) as file:
        file_contents = file.read()

    return file_contents


def main():
    file_contents = get_book_text("./books/frankenstein.txt")

    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")

    character_counts = get_character_counts(file_contents)
    print(character_counts)

    sorted_dictionary = get_sorted_dictionary(character_counts)
    for detail in sorted_dictionary:
        if detail["char"].isalpha():
            print(f"{detail['char']}: {detail['num']}")


main()

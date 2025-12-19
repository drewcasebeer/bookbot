from typing import Any


def get_num_words(text: str):
    return len(text.split())


def get_character_counts(text: str):
    character_counts: dict[str, int] = {}

    characters = list(text.lower())

    for character in characters:
        if character not in character_counts:
            character_counts[character] = 0

        character_counts[character] += 1

    return character_counts


def sort_on_num(items):
    return items["num"]


def get_sorted_dictionary(dict: dict[str, int]):
    sorted_dictionarys = []

    for key in dict:
        sorted_dictionarys.append({"char": key, "num": dict[key]})

    sorted_dictionarys.sort(reverse=True, key=sort_on_num)

    return sorted_dictionarys

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

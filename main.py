#! /usr/bin/python
"""
This is the main module for bookbot project
"""


import re


def count_words(file):
    """
    Returns the number of words in a string
    """
    return len(file.split())


def file_handler(path):
    """
    Opens a file in read mode or handle FileNotFoundError
    """
    try:
        with open(path, "r", encoding="UTF-8") as f:
            file_handle = f.read()
            return file_handle
    except FileNotFoundError:
        return print(f"The file : {path} cannot be found")


def count_character_occurrence(text):
    """
    Count character occurence in text. Returns a dict
    """
    lowered_text = text.lower()
    character_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    for key in character_dict:
        for c in lowered_text:
            if c == key:
                character_dict[key] += 1
    return character_dict


def rank_character_occurrence(character_dict: dict):
    sorted_dict = {}
    for key in sorted(character_dict, key=character_dict.get, reverse=True):
        sorted_dict[key] = character_dict[key]
    return sorted_dict


def main():
    """
    The main function is opening a hard-coded .txt file
    """
    text_path = "./books/frankenstein.txt"
    file_handle = file_handler(text_path)
    print(file_handle)
    word_count = count_words(file_handle)
    print(f"---------- REPORT OF {text_path} ----------\n")
    print(f"The number of words is {word_count} \n")
    character_occurrence_count = count_character_occurrence(file_handle)
    ranked_characters_by_highest_occurrence = rank_character_occurrence(
        character_occurrence_count
    )
    for key, value in ranked_characters_by_highest_occurrence.items():
        print(f"The character {key} was found {value} times")
    print("\n---------- END OF REPORT ----------")


if __name__ == "__main__":
    main()

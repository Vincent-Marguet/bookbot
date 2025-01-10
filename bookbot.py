#! /usr/bin/python
"""
This is the main module for bookbot project
"""


import argparse
import sys


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
        return print(f"\nERROR: The file : {path} cannot be found\n")


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
    parser = argparse.ArgumentParser(
        prog="python3 bookbot.py",
        description="Bookbot : a basic bot to analyze or print text files",
        epilog="---------- END OF HELP ----------",
    )
    parser.add_argument("FILE")
    parser.add_argument(
        "-c",
        "--count",
        help="Displays word count for FILE",
    )
    parser.add_argument(
        "-cc",
        "--char-count",
        help="Displays character count for each alphabetic UTF-8 character from FILE",
    )
    parser.add_argument(
        "-r",
        "--char-ranked",
        help="Displays the descending sorted character count for each alphabetic UTF-8 character from FILE",
    )
    parser.add_argument("-p", "--print", help="Print the entire FILE on screen")

    try:
        text_path = sys.argv[1]
        file_handle = file_handler(text_path)
        if len(sys.argv) > 2:
            for i in range(2, len(sys.argv)):
                if (
                    sys.argv[i] != "-p"
                    and sys.argv[i] != "-cc"
                    and sys.argv[i] != "-r"
                    and sys.argv[i] != "-c"
                ):
                    parser.print_help()
                    return

                if sys.argv[i] == "-p":
                    print(file_handle)
                    print("\n")
            print(f"\n---------- REPORT OF {text_path} ----------\n")
            for i in range(2, len(sys.argv)):
                if sys.argv[i] == "-c":
                    word_count = count_words(file_handle)
                    print(f"The number of words is {word_count}\n")
                elif sys.argv[i] == "-cc":
                    counted_char_dict = {}
                    counted_char_dict = count_character_occurrence(file_handle)
                    for key, value in counted_char_dict.items():
                        print(f"The character {key} has been found: {value} times")
                elif sys.argv[i] == "-r":
                    character_occurrence_count = count_character_occurrence(file_handle)
                    ranked_characters_by_highest_occurrence = rank_character_occurrence(
                        character_occurrence_count
                    )
                    for (
                        key,
                        value,
                    ) in ranked_characters_by_highest_occurrence.items():
                        print(f"The character {key} was found {value} times")
            print("\n---------- END OF REPORT ----------")
        else:
            parser.print_help()
            return
    except argparse.ArgumentError as a:
        print(a)
    except IndexError:
        parser.print_help()


if __name__ == "__main__":
    main()

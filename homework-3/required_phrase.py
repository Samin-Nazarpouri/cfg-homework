"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""
from itertools import islice

def generate_phrase(characters, phrase):
    characters = list(islice(characters, len(characters)))
    phrase = list(islice(phrase, len(phrase)))
    for i in characters:
        num_of_item_in_characters = characters.count(i)
        if i in phrase and num_of_item_in_characters == phrase.count(i):
            return True
        else:
            return False


# Exercise example
print(generate_phrase('cbacba','aabbccc'))

# Example of empty string
print(generate_phrase(' ', ' '))

# Example of any characters
print(generate_phrase('-pa 3le!', '3le-a !p'))


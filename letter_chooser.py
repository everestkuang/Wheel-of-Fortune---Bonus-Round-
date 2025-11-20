import string
from collections import Counter

DEFAULT_GIVEN = set("RSTLNE")

def choose_optimal_letters(puzzle_list):
    """
    Compute frequency of remaining consonants and vowels
    after eliminating R S T L N E.
    """
    letters = Counter("".join(puzzle_list).replace(" ", "").upper())
    
    consonants = [c for c in string.ascii_uppercase if c not in "AEIOU" and c not in DEFAULT_GIVEN]
    vowels = [v for v in "AEIOU" if v not in DEFAULT_GIVEN]

    top_consonants = sorted(consonants, key=lambda c: letters[c], reverse=True)[:3]
    top_vowel = max(vowels, key=lambda v: letters[v])

    return top_consonants, top_vowel

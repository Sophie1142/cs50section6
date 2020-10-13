# Revisiting Anagram from section 2

# Write a program anagram.c that takes two words as input,
# and determines whether the words are anagrams of one another.
# - If two words are an exact match (the strings are identical, ignoring case),
#     the program should output EXACT MATCH.
# - If either word contains non-alphabetic characters, the program should
#     output Alphabetic characters only and return 1.
# - Otherwise, if two words consist of only alphabetic characters, the
#     program should check to see if the letters in the first word can
#     be rearranged (ignoring case) to form the second word. If so,
#     the program should print ANAGRAM; if not, the program should print NOT ANAGRAM.


# Use the bountiful resources available to you within Python!

import csv
import sys

# https://www.geeksforgeeks.org/python-sorted-check-two-strings-anagram-not/
# referenced used for the sorted function

if len(sys.argv) != 3:
     sys.exit("Usage: python anagram.py word1 word2")

# Cast to string and make all lowercase
word1 = str(sys.argv[1]).lower()
word2 = str(sys.argv[2]).lower()

# Check lengths (NOTE: Could make a case for not checking the length in the first place)
if len(word1) != len(word2):
    sys.exit("NOT ANAGRAM")

# Check if exact match
if word1 == word2:
    sys.exit("EXACT MATCH")
elif sorted(word1) == sorted(word2):
    sys.exit("ANAGRAM")
else:
    sys.exit("NOT ANAGRAM")
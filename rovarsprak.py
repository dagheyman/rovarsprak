#!/usr/bin/env python3

import fileinput

CONSONANTS = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]

def parse(text):
    result = ""
    for line in text:
        result += _parse_line(line)
    return result

def _consonant(letter):
   return letter.lower() in CONSONANTS

def _add_o(letter):
    return letter + "o" + letter.lower()

def _parse_line(line):
    new_line = ""
    for letter in line:
        if _consonant(letter):
            new_line += _add_o(letter)
        else:
            new_line += letter
    return new_line

if __name__ == "__main__":
    print(parse(fileinput.input()))

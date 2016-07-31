#!/usr/bin/env python3

import fileinput

CONSONANTS = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

def parse(text):
    return ''.join([_parse_line(line) for line in text])

def _parse_line(line):
    return ''.join([_parse_letter(letter) for letter in line])

def _parse_letter(letter):
    return _add_o(letter) if _consonant(letter) else letter

def _add_o(letter):
    return letter + "o" + letter.lower()

def _consonant(letter):
    return letter.lower() in CONSONANTS

if __name__ == "__main__":
    print(parse(fileinput.input()))

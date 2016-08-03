#!/usr/bin/env python3

import fileinput

CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']


def parse(text):
    return ''.join(_parse_char(char) for char in text)


def unparse(text):
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i].lower() in CONSONANTS:
            i += 3
        else:
            i += 1
    return result


def _parse_char(char):
    return char + 'o' + char.lower() \
        if char.lower() in CONSONANTS else char

if __name__ == "__main__":
    for line in fileinput.input():
        print(parse(line))

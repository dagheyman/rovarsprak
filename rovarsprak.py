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
        if _consonant(text[i]):
            i += 3
        else:
            i += 1
    return result


def verify(text):
    i = 0
    while i < len(text):
        if _consonant(text[i]):
            try:
                if text[i + 1].lower() != "o":
                    return False
                if text[i + 2].lower() != text[i].lower():
                    return False
                i += 3
            except IndexError:
                return False
        else:
            i += 1
    return True


def _parse_char(char):
    return char + 'o' + char.lower() \
        if _consonant(char) else char


def _consonant(char):
    return char.lower() in CONSONANTS

if __name__ == "__main__":
    for line in fileinput.input():
        print(parse(line))

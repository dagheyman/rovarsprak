import fileinput

CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']


def parse(text):
    return ''.join(_parse_char(char) for line in text for char in line)


def _parse_char(char):
    return char + 'o' + char.lower() \
        if char.lower() in CONSONANTS else char

if __name__ == "__main__":
    print(parse(fileinput.input()))

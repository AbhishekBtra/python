from itertools import dropwhile


with open('sample txts/lorem.txt') as f:
    for line in dropwhile(lambda line : line.startswith('#'),f):
        print(line) # skips the comments starting with #
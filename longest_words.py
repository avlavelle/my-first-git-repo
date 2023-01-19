

words = []

with open('words','r') as infile:
    words = infile.read().splitlines()


words.sort(key=len, reverse = True)

print(words[:5])

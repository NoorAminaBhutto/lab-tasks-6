words = ['apple', 'ant', 'banana', 'ball', 'cat']

mydict = {}

for word in words:
    letter = word[0]

    if letter in mydict:
        mydict[letter].append(word)
    else:
        mydict[letter] = [word]

print(mydict)
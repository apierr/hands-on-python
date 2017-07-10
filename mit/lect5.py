"""
Objects in python
Tuples, Lists, and Dictionaries
"""

EtoF = {'bread': 'du pain', 'wine': 'du vin',\
       'eats': 'mange', 'drinks': 'bois',\
       'likes': 'aime', 1: 'un',\
       '6.00':'6.00'}

def translateWord(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    return word

def translate(sentence):
    translation = ''
    word = ''
    for c in sentence:
        if c != ' ':
            word = word + c
        else:
            translation = translation + ' ' + translateWord(word, EtoF)
            word = ''
    return translation + ' ' + translateWord(word, EtoF)

print translate('John eats bread')
print translate('Steve drinks wine')
print translate('John likes 6.00')
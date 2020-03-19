# Python 3 & above

"""Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." 
So "Python" becomes "ythonpay." To write a Pig Latin translator in Python"""

pyg = 'ay'

original = input('Enter a word:')
word = original.lower()
word = str(word)
word = word.strip()
first = word[0] 

if len(original) > 0 and original.isalpha(): #AllCharacters
    print(original)
else:
    print('empty')
    
new_word = word + first + pyg
new_word = new_word[1:]
print(new_word)


# Write code that will print out the anagrams (words that use the same letters) from a paragraph of text.

paragraph = input('Enter paragraph: ')

textList = paragraph.split()

for text in textList:
    textLen = len(text)
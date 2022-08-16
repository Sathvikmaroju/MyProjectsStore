import json
from difflib import get_close_matches

def translate(word_):
    if word_.lower() in data:
        return data[word_.lower()]
    elif word_.title() in data:
        return data[word_.title()]
    elif word_.upper() in data:
        return data[word_.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean '%s' instead"%get_close_matches(word,data.keys())[0])
        decide = input("y/n  ")
        if decide == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == 'n':
            return 'No such word found.'
        else:
            return "Enter y/n "
    else:
        return "No such word found."

data = json.load(open("data.json"))

word = input('Enter word - ')
output = translate(word)
if output != "No such word found.":
    if len(output) > 1:
        print("\nMeanings :")
        for i in output:
            print("    ",output.index(i)+1, "-", i)
    else:
        print('\nMeaning -  ',output[0])
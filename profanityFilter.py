from better_profanity import profanity

profanity.load_censor_words()
x=input("Enter a sentence")
output = profanity.censor(x)
print(output)
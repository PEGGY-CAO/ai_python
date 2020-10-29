# USE THE python TextBlob library to create a language translation application.
# Your application should accept at least two input from the user.
# The first input should be the text to be translated (your program should accept any language).
# The second should be the language to translate to.
# At minimum, your program should be able to translate to 10 different languages.
# Your program must have at least one python function

from textblob import TextBlob

def translate(textInput, lang):
    # translate and print
    blob = TextBlob(textInput)
    print(blob.translate(to=langInput))

    return


textInput = input("Please input sentences for translation:")
langInput = input("Input the language code you want to translate to:")


translate(textInput, langInput)


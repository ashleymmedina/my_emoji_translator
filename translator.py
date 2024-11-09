from emoji_translate.emoji_translate import Translator
import random

emo = Translator(exact_match_only=False)

emoji = {
    "happy" : "😄",
    "sad" : "😔" ,
    "funny" : "😂",
    "side eye" : "👀",
    "funny" : "😭",
    "oh-" : "😕",
    "idk" : "🤷🏽‍♀️", 
    "okay" : "🫡",
    "like" : "🥰", 
    # "like" : "🤭",
    # "like" : "😘",
    "love" : "😍",
    "love" : "❤️",
    "don't" : "❌",
    "don't" : "🙅‍♂️",
    "don't" : "🙅‍♀️",
    "dogs" : "🐶",
    "dog" : "🐾",
    "cat" : "🐱",
    "cats" : "😸",
    "excited" : "🤗",
    "thank you" : "😊",
    "appreciate" : "😊",
    "beautiful" : "🤩",
    "beautiful" : "😍",
    "butterfly" : "🦋",
    "butterflies" : "🦋",
    "ghetto" : "", 
    "cool" : "😎", 
    "cool" : "👍", 
    "wow" : "", 
    "wow" : "", 
    "" : "", 
    "" : "", 
    "" : "", 
    "" : "", 
    "" : "", 
}


while True:
    inp = input("Enter a sentence: ")
    words = inp.split(' ')
    emojified = ""
    for word in words:
        if word in emoji:
            emojified += emoji[word]
        else:
            emojified += word
        emojified += " " 

    print(emojified)

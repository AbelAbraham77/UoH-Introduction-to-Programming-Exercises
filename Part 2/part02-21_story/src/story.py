story=""
lword=""
while True:
    word=input("Please type in a word: ")

    if word=="end":
        break 
    
    if word==lword:
        break 

    story = story + " " + word
    lword=word

print(story)


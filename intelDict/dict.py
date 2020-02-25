import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) >0:
        yN = input("Did you mean %s instead? Enter Y if Yes, or N if No:" % get_close_matches(w, data.keys())[0])
        if yN == "Y":
            return data[get_close_matches(w, data.keys()) [0]]
        elif yN == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "Please Enter Y or N."
    else:
        return "The Word you entered doesn't exist!\nPlease double check it!"

word = input("Enter Word: \n")

outPut = translate(word)

if type(outPut) == list:
    for item in outPut:
        print("--", item)
else:
    print("--", outPut)
import json
from difflib import get_close_matches

data = json.load(open('names.json', 'r'))

def get_meaning(word: str):
    if word in data.keys():
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        usr_input = input('Do you mean %s instead? Enter y if yes, or n if no: ' %get_close_matches(word, data.keys())[0])
        # take yes or no input
        if usr_input == 'y' or 'yes' or 'Yes' or 'Y':
            return get_close_matches(word, data.keys())[0]
        elif usr_input == 'n' or 'N' or 'No' or 'no':
            pass
    else:
        print(f'{word} is not registerd with us!!!')
        


word = input('Enter your word: ')
ouput = get_meaning(word)
print(ouput)
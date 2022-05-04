# Libraries
import json
from difflib import SequenceMatcher, get_close_matches

# Data variable
data = json.load(open("recipes.json"))

keys = data.keys()

# List of keys
def get_recipe(word):
	word = word.title()
	while True:
		if word in data:
			return data[word]
		elif len(get_close_matches(word, keys)) > 0:
			response2 = input("Did you mean %s? " % get_close_matches(word, data.keys())[0] + "Y/N ")
			response2 = response2.upper()
			if response2 == "Y":
				return data[get_close_matches(word, data.keys())[0]]
			elif response2 == "N":
				return "Sorry we can't find your item today."
			else:
				return "Apologies, please contact us for support."
		else:
			return ("Sorry, " + word + " is not in our recipe list. Please try again. ")


food_item = input("What do you want to eat? ")
response = print(get_recipe(food_item))
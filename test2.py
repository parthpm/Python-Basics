#Pig Latin - Pig Latin is a game of alterations played on the English language game.
# To create the Pig Latin form of an English word
# the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay).



def piglatin(check):

    initial=str(check[0])
    del check[0]
    check.extend([initial,'a','y'])

    pig=''.join(check)
    pig=pig.lstrip('')
    return pig

check=input("Enter the word to create pig latin form").lower()
check=list(check)

p=piglatin(check)
print(p)


#or
import
def pig_latin(string):
	string = string.lower()
	consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
	first_letter = string[0]
	pig_latin = ''
	for consonant in consonants:
		if first_letter == consonant:
			pig_latin = string.split(consonant, 1)[1] + first_letter +"ay"
			return pig_latin
	else:
		pig_latin = string + "way"
		return pig_latin

print pig_latin("Banana")
print pig_latin("example")
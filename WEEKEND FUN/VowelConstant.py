letter = input("Enter an Alphabet: ").lower()
vowels =  ("a","e","i","o","u")

if ( (not letter.isalpha())):
     print("Invalid Input, Input only Alphabet")
elif (letter in vowels):
          print("The Alphabet is a Vowel")
else:
     print("The Alphabet is a Consonant")
    




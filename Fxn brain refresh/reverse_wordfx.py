def reverse_word(word):
     return word[-1::-1]



#word = input("Enter a word: ")
#print("Reversed word:", reverse_word(word))




def vowel_checker(string):
     lenght=""     
     vowel= "a","e","i","o","u"
     for word in string:
          if word in vowel and word not in lenght:
#          if string[word] == vowel:
               lenght+=word
               
     return len(lenght)


print(vowel_checker("adagoestoschool"))

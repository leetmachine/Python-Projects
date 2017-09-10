
#A function to remove all vowels from a string
def disemvowel(word):
    vowels = ["a","e","i","o","u"]

    word = list(word)

    for vowel in vowels:
        while vowel in word:
            word.remove(vowel)
        
        while vowel.upper() in word:
            word.remove(vowel.upper())
    
    return ''.join(word)


#examples
#print(disemvowel('azEziAzoU'))
#print(disemvowel('bbbb'))
#print(disemvowel('aAaeEeEEiOz'))
print("A program to remove all vowels from a string.")
phrase = input("Enter a string: ")
print(disemvowel(phrase))
#
#def stringlen(string):
#    count = 0
#    for char in string:
#        count = count + 1 
#    return count
#print(stringlen("Adeolu"))
#
#
#def reverse(string):
#    length = len(string)
#    for length in range(length, 0 , -1):
#        print(reverse("Ade"), " ")
#       
#    

def vowel(words):
   
    vowel = ["a","e","i","o","u"]
    count = 0
    for char in vowel:
        for char2 in words:
            if(vowel[count]== char2):
                count = count + 1
    return count

words = "pineapple"
print(vowel(words))

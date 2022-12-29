word_check = input("Please, enter the word: ")

def palindrome(word_check):
    if len(word_check) <= 1:
        return True
    else:
        return word_check[0] == word_check[-1] and palindrome(word_check[1:-1])

print(palindrome(word_check))

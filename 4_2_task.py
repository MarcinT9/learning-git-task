def is_palindrome(word):
    if word[::-1] == word:
        return True
    else:
        return False

print(is_palindrome('kajak'))
print(is_palindrome('Marcin'))
print(is_palindrome('malajalam'))
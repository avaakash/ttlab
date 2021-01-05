def is_palindrome(string):
    return string == string[::-1]


string = str(input("Enter text: "))

if(is_palindrome(string)):
    print('%s is palindrome' %string)
else:
    print("%s is not palindrome" %string)
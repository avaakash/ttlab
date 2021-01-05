def check_palindrome(number):
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if number == sum:
        return True
    return False

number = int(input("Enter a number: "))

if check_palindrome(number) :
   print(number," is an Armstrong number")
else:
   print(number," is not an Armstrong number")
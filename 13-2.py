def is_palindrome(s):
    s = str(s)
    return s == s[::-1]


def generate_palindrome(number):
    palindromes = [i for i in range(1, number) if is_palindrome(i)]
    return palindromes


print(generate_palindrome(200))

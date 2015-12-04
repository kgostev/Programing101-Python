def sum_of_digits(n):
    sum_of_digits = 0
    if n < 0:
        n *= -1

    while n / 10 > 0:
        sum_of_digits += n % 10
        n //= 10
    return sum_of_digits


print("1. sum of digits", sum_of_digits(1234))


def to_digits(n):
    return [int(x) for x in str(n)]

print("2. to digits", to_digits(123))


def count_digits(n):
    counter = 0

    for i in str(n):
        counter += 1

    return counter


def to_number(digits):
    result = 0

    for digit in digits:
        power = count_digits(digit)
        result = result * (10 ** power) + digit

    return result


print("3. to number", to_number([1, 2, 3]))


def fact_digits(n):
    digits = to_digits(n)
    s = 0
    for d in digits:
        s += fact(d)
    return s


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print("4. Fact digits: ", fact_digits(145))


def fibonacci(n):
    result = []
    a, b = 1, 1

    while len(result) < n:
        result.append(a)
        a, b = b, a + b

    return result

print("5. fibonacci", fibonacci(10))


def fib_number(n):
    return to_number(fibonacci(n))


print("6. fib number", fib_number(10))


def palindrome(obj):
    return str(obj) == str(obj)[::-1]


print("7. palindrome", palindrome("kapak"))


def count_vowels(s):
    result = 0

    for ch in s.lower():
        if ch in "aeiouy":
            result += 1

    return result

print("8. count vowels", count_vowels("kapak"))


def count_consonants(s):
    result = 0

    for ch in s.lower():
        if ch in "qwrtplkjhgfdszxcvbnm":
            result += 1

    return result

print("8. count consonants", count_consonants("kapak"))


def char_histogram(s):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic


print("9. char histogram", char_histogram("AAAAaaa!!!"))

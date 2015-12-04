import itertools


def is_number_balanced(n):
    if len(str(n)) == 0:
        return True
    n = str(n)
    left = n[0:(len(n) // 2)]
    right = n[(len(n) // 2)::]
    leftSum = 0
    rightSum = 0
    for i in left:
        leftSum += int(i)
    for i in right:
        rightSum += int(i)
    return leftSum == rightSum

print("Task 1", is_number_balanced(4518))


def is_increasing(seq):
    current = seq[0]
    for i in range(0, len(seq)):
        if(current >= seq[i] and i != 0):
            return False
    return True


print("Task 2.1", is_increasing([1, 2, 3, 4, 5, 6]))


def is_decreasing(seq):
    current = seq[0]
    for i in range(0, len(seq)):
        if(current <= seq[i] and i != 0):
            return False
    return True

print("Task 2.2", is_decreasing([3, 2, 1]))


def palindrome(obj):
    obj = str(obj)
    return obj == obj[::-1]


def get_smallest_palindrome(n):
    if(n < 0):
        return "Error"
    while True:
        n -= 1
        if palindrome(n):
            return n

print("Task 3", get_smallest_palindrome(12345))


def prime_numbers(n):
    lci = []
    for i in range(2, n):
        lci.append(i)

    for i in range(2, len(lci)):
        for j in range(i, n, i):
            if j != i and j in lci:
                lci.remove(j)
    return lci

print("Task 4", prime_numbers(30))


def is_anagram(a, b):
    b = str(b)
    if(len(a) == len(b)):
        for i in range(0, len(a)):
            if a[i].lower() not in b.lower():
                return False
    return True

print("Task 5", is_anagram("BraDe", "Beard"))


def birthday_ranges(birthdays, ranges):
    result = []
    for i in range(0, len(ranges)):
            result.append(0)

    for i in range(0, len(ranges)):
        for j in range(0, len(birthdays)):
            if birthdays[j] in range(ranges[i][0], ranges[i][1]):
                result[i] += 1
    return result


birthdays = [5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15]
ranges = [(4, 9), (6, 7), (200, 225), (300, 365)]

print("Task 6", birthday_ranges(birthdays, ranges))


def sum_matrix(m):
    sum_of_matrix = 0
    for i in m:
        sum_of_matrix += sum(i)
    return sum_of_matrix

print("Task 7", sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def matrix_bombing_plan(m):
    dic = {}
    temp_sum = 0
    temp_matrix = []
    whole_matrix_sum = sum_matrix(m)
    dmg = 0
    demaged_matrix = []

    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            dic[(i, j)] = 0

    for i in range(0, len(m)):
        for j in range(0, len(m[i])):

            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                        if x >= 0 and y < len(m[i]) and x < len(m[j]) and y >= 0:
                            temp_matrix.append(m[x][y])
                            if m[x][y] - m[i][j] >= 0:
                                demaged_matrix.append(m[x][y] - m[i][j])
                            else:
                                demaged_matrix.append(0)
                            if m[i][j] in temp_matrix:
                                temp_matrix.remove(m[i][j])

            dmg = sum(temp_matrix) - sum(demaged_matrix)
            dic[(i, j)] = whole_matrix_sum - dmg
            temp_matrix = []
            temp_sum = 0
            dmg = 0
            demaged_matrix = []
    return dic


print("Task 8", matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def is_transversal(transversal, family):
    trans_counter = 0
    for i in transversal:
        for j in family:
            if i in j:
                trans_counter += 1
    return trans_counter == len(transversal)

print("Task 9.1: ", is_transversal((4, 5, 6), ((5, 7, 9), (1, 4, 3), (2, 6))))


def generate_transversal(family):
    transversals = []
    for t in itertools.product(*family):
        if is_plurality(t):
            transversals.append(t)
    return transversals


def is_plurality(m):
    for i in range(0, len(m)):
        for j in range(i, len(m)):
            if m[i] == m[j] and i != j:
                return False
    return True

print("Task 9.2", generate_transversal([[1, 4, 5], [2, 7], [1, 9]]))

def count_words(arr):
    dic = {}
    counter = 0
    for j in arr:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1
    return dic

print("Task 1", count_words(["python", "python", "python", "ruby"]))


def nan_expand(times):
    s = ""
    notA = "Not a "
    nan = "NaN"

    for i in range(0, times):
        s += notA
    if times > 0:
        s += nan
    return s

print("Task 2", nan_expand(3))


def iterations_of_nan_expand(expanded):
    counter = 0

    for i in range(0, len(expanded), 3):
        # print(expanded[i : i + 3])
        if expanded[i: i + 3] == "Not":
            counter += 1
    if expanded != nan_expand(counter):
        return False
    else:
        return counter

print("Task 3", iterations_of_nan_expand("Not a Not a Not a NaN"))


def group(items):
    group = []
    grouped_items = []

    for i in range(0, len(items) - 1):
        if items[i] == items[i + 1]:
            group.append(items[i])
        else:
            group.append(items[i])
            grouped_items.append(group)
            group = []
        if i == len(items) - 2:
            group.append(items[i + 1])
            grouped_items.append(group)

    return grouped_items


print("Task 4", group([1, 1, 1, 2, 3, 4, 4, 4, 5, 4, 4, 4, 5, 4]))


def max_consecutive(items):
    max = 0
    counter = 0

    grouped_items = group(items)
    for i in grouped_items:
        if len(i) > max:
            max = len(i)

    return max

print("Task 5", max_consecutive([1, 2, 3, 3, 3, 3, 5, 5, 5, 5, 5]))


def gas_stations(distance, tank_size, stations):
    gas = tank_size
    stops = stations
    stations_to_stop = []

    for i in range(0, len(stops) - 1):
        gas -= stops[i]
        if gas < stops[i + 1]:
            stations_to_stop.append(stops[i + 1])
        if stops[i] == stations_to_stop[i]:
            gas = tank_size
    return stations_to_stop


print("Task 6", gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))


def sum_of_numbers(st):
    counter = 0
    sum_ = 0
    for i in st[::-1]:
        if i.isdigit():
            sum_ += int(i) * 10 ** counter
            counter += 1
        else:
            counter = 0
    return sum_


print("Task 7", sum_of_numbers("1asd2asd3"))


def number_to_message(message):
    dic = {'2': 'a', '3': 'd', '4': 'g', '5': 'j', '6': 'm', '7': 'p', '8': 't', '9': 'w'}
    max_presses = {'2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 5, '8': 4, '9': 5}
    grouped = group(message)
    to_upper = False
    msg = ""
    for i in grouped:
        if i[0] == -1:
            pass
        elif i[0] == 0:
            for j in i:
                msg += ' '
        elif i[0] == 1:
            to_upper = True
        else:
            if len(i) > max_presses[str(i[0])]:
                msg += chr(ord(dic[str(i[0])]) + len(i) - 1 - max_presses[str(i[0])])
            elif len(i) == max_presses[str(i[0])]:
                print(i[0])
                msg += str(i[0])
            else:
                if to_upper:
                        msg += chr(ord(dic[str(i[0])]) + len(i) - 1).upper()
                        to_upper = False
                else:
                    msg += chr(ord(dic[str(i[0])]) + len(i) - 1)
    return msg


print("Task 8.1", number_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]))


def message_to_number(message):
    dic = ['abc2', 'def3', 'ghi4', 'jkl5', 'mno6', 'pqrs7', 'tuv8', 'wxyz9', ' ']
    message_numbers = []
    prev = message[0]
    counter = 0

    for i in message:
        for j in dic:
            if i.lower() in j:
                if ord(i) >= 65 and ord(i) <= 90:
                    message_numbers.append(1)
                    for x in range(0, j.index(i.lower()) + 1):
                        message_numbers.append(dic.index(j) + 2)
                elif i == ' ':
                    message_numbers.append(0)
                elif prev in j and counter > 0:
                    message_numbers.append(-1)
                    for x in range(0, j.index(i) + 1):
                        message_numbers.append(dic.index(j) + 2)
                else:
                    for x in range(0, j.index(i) + 1):
                        message_numbers.append(dic.index(j) + 2)
                    # print(j.index(i), dic.index(j))
        prev = i
        counter = 1
    return message_numbers

print("Task 8.2", message_to_number("Ivo e Panda"))

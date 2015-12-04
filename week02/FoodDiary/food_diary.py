import time
import json


def main():
    menu()


def menu():
    print("Hello and welcome")
    while True:
        print("Choose an option")
        print("1. meal - write what are you eating now")
        print("2. list <dd.mm.yyyy> - list all your meals")
        command = input("Enter command>")
        print(command)
        command_list = command.split()
        if command_list[0] == 'meal':
            input_meal(command_list[1:])
            calory_counter(command_list[1:])
        elif command_list[0] == 'list':
            print_meals(command_list[1:])
        else:
            print("Error")


def input_meal(meal):
    data = open("meals.txt", 'a+')
    if date_exsists(data):
        data.write(''.join(meal) + ' ')
    else:
        data.write(time.strftime("%d.%m.%Y" + ' ' + ''.join(meal) + ' '))
    data.close()


def date_exsists(data):
    data = open("meals.txt", 'r')
    date = time.strftime("%d.%m.%Y")
    lines = data.read()
    data.close()
    return date in lines


def print_meals(date):
        data = open("meals.txt", 'r')
        lines = data.readlines()

        for line in lines:
            if ''.join(date) in line:
                split_line = line.split()
                for i in split_line:
                    print(i)


def calory_counter(meal):
    if in_database(meal[0]):
        print("True")
        count_calories(meal)
    else:
        print(meal[0], "False")
        add_in_db(meal[0])
        count_calories(meal)


def in_database(meal):
    with open('calories.json', 'r') as f:
        data = json.load(f)
    if meal in data:
        f.close()
        return True
    else:
        f.close()
        return False


def count_calories(meal):
    f = open('calories.json', 'r')
    data = json.load(f)
    value = get_value(meal[1])
    if 'kg' in meal[1]:
        value *= 1000
    print('Ok, this is total of', value / 100 * data[meal[0]], 'calories for this meal')
    f.close()


def add_in_db(meal):
    f = open('calories.json', 'r')
    data = json.load(f)
    f.close()

    print('I don\'t have icecream in the calories database.')
    calories = input('How much calories per 100g? >')

    data.update({meal: int(calories)})

    f = open('calories.json', 'w')
    json.dump(data, f)
    f.close()


def get_value(st):
    counter = 0
    number = 0
    for i in st[::-1]:
        if i.isdigit():
            number += int(i) * 10 ** counter
            counter += 1
        else:
            counter = 0
    return number

if __name__ == '__main__':
    main()

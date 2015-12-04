import json


def read_json():
    f = open('data.json', 'r')
    data = json.load(f)

    skills = get_skills(data)
    print_best(skills, data)


def get_skills(data):
    all_skills = []

    for people in data['people']:
        for skills in people['skills']:
            if skills['name'] not in all_skills:
                all_skills.append(skills['name'])
    return all_skills


def get_best(skill, data):
    max_skill = 0
    name = ''

    for people in data['people']:
        for skills in people['skills']:
            if skills['name'] == skill:
                if skills['level'] > max_skill:
                    max_skill = skills['level']
                    name = people['first_name'] + ' ' + people['last_name']

    return name


def print_best(skills, data):
    for skill in skills:
        print(skill, get_best(skill, data))


read_json()

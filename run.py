import sys
import re
import json

path = 'data.txt'
t_split = r'[\t\-\;]+'
t_id = 'id', '[1-9][0-9]*'
t_name = 'name', '[a-zA-Z]+'
t_age = 'age', '[1-9][0-9]*'
t_phone = 'phone', '[\+|0-9][0-9]{,11}'
t_email = 'email', '[a-zA-Z0-9]{1,}@[a-zA-Z]{1,}\.[a-zA-Z]{1,}'
t_role = 'role', '(admin|user|guest){1}'
t_status = 'status', '(in)?active'
t_list = [t_id, t_name, t_age, t_phone, t_email, t_role, t_status]

def save_json(dictionary, filename='data.json'):
    with open(filename, 'w') as ff:
        json.dump(dictionary, ff, indent=2)

def method():
    with open(path, 'r') as f:
        persons = []
        lines = f.readlines()
        for line in lines[1:]:
            data = re.split(t_split, line)
            person = {}
            for ind, value in enumerate(data[:-1]):
                person[t_list[ind][0]] = value if re.fullmatch(t_list[ind][1], value) else None
            persons.append(person)
    return(persons)

def start():
    print(method())
    save_json(method())

if __name__ == '__main__':
   start()
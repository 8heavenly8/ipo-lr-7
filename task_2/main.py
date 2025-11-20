import json
with open ('dump.json', 'r', encoding="utf-8") as dump:
    content = json.load(dump)  
    number = input("введите номер квалификации: ")
    if ('code' in content[int(number)]['fields'] and 'title' in content[int(number)]['fields']):
        print(f"{content[int(number)]['fields']['code']} {content[int(number)]['fields']['title']}")
    else:
        print
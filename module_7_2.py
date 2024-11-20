from pprint import pprint

def custom_write(file_name, strings):
    string_positions = {}
    n = 0

    for string in strings:
        n += 1
        file = open(file_name, 'a', encoding = 'utf-8')
        key = (n, file.tell())
        file.write(f'{string}\n')
        file.close()
        string_positions[key] = string

    return string_positions


info = [
'Text for tell.',
'Используйте кодировку utf-8.',
'Because there are 2 languages!',
'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

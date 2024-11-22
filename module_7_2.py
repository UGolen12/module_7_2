from pprint import pprint


def custom_write(file_name, strings):
    string_positions = {}
    n = 0
    file = open(file_name, 'w', encoding='utf-8')

    for string in strings:
        n += 1
        key = (n, file.tell())
        file.write(f'{string}\n')
        string_positions[key] = string

    return string_positions
    file.close()


info = [
'Text for tell.',
'Используйте кодировку utf-8.',
'Because there are 2 languages!',
'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

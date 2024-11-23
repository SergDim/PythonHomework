

def custom_write(file_name, strings):
    file = open(file_name, mode = 'w', encoding = 'utf-8')
    dict_positions_str = {}
    for i in range(len(strings)):
        dict_positions_str.update({(i+1,file.tell()) : strings[i]})
        file.write(strings[i])
        file.write('\n')
    file.close()
    return dict_positions_str


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
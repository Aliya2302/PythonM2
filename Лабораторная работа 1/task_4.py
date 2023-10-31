users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
total_number = len(users)
unique_number = len(set(users))
dict_ = {
    'Общее количество': '0',
    'Уникальные посещения': '0'
}
dict_['Общее количество'] = total_number
dict_['Уникальные посещения'] = unique_number
print(dict_)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

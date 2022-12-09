with open("task3.txt", encoding="utf-8") as f_obj:
    strings = f_obj.readlines()
dict_people = {s.split(' ').pop(0): float(s.split().pop(1)) for s in strings}
less_twenty = list((surname[0] for surname in dict_people.items()
                    if surname[1] < 20000))
print(f'Сотрудники с окладами менее 20 тыс:\n{less_twenty}')
print(f'Средняя величина дохода сотрудника: '
      f'{sum(dict_people.values())/len(dict_people)}')

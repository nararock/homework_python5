with open("task2.txt") as f_obj:
    strings = f_obj.readlines()
amount_string = len(strings)
amount_words = len(list((word for s in strings for word in (s.split(' ')))))
print(f"Количество строк: {amount_string};\nколичество слов: {amount_words}")

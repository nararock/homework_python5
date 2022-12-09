with open('task1.txt', 'w', encoding='utf-8') as f_obj:
    strings = []
    while True:
        my_string = input("Введите строку: ")
        if my_string == "":
            break
        print(my_string, file=f_obj)

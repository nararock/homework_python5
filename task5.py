with open("task5.txt", 'w', encoding="utf-8") as f_obj:
    numbers = input("Введите числа через пробел: ")
    print(numbers, file=f_obj)

with open("task5.txt", 'r', encoding="utf-8") as f_obj:
    my = list(float(el) for el in (f_obj.read().split(' ')))
    print(sum(my))





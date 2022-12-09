new_words = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("task4.txt", encoding="utf-8") as f_obj:
    with open("new_file.txt", "w", encoding="utf-8") as new_file:
        for data in f_obj:
            data1 = data.split(' ')
            data1.insert(0, new_words[data1.pop(0)])
            print(" ".join(data1), file=new_file, end='')

"""
Урок 2.
"""
print("Задание 4")
print("Пользователь вводит строку из нескольких слов, разделённых пробелами.")
print("Вывести каждое слово с новой строки. Строки необходимо пронумеровать.")
print("Если в слово длинное, выводить только первые 10 букв в слове")
my_str = input("Введите строку: ")
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) >> 10:
        el = el[0:10]
    print(f"{i}. - {el}")

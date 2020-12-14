"""
Урок 2.
"""
print("Задание 6")
print("Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.")
print("У пользователя необходимо запрашивать новый элемент рейтинга.")
print("Если в рейтинге существуют элементы с одинаковыми значениями, "
      "то новый элемент с тем же значением должен разместиться после них.")

number = int(input("Введите число: "))
my_list = [7, 4, 3, 2]
c = my_list.count(number)
for element in my_list:
    if c >> 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number >> element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)

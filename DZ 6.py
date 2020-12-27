# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:08:58 2020

@author: Александр Терещук
"""

# 1. Дан список строк my_list. Создать новый список 
# в который поместить элементы из my_list по следующему
# правилу: Если строка стоит на нечетном месте в my_list, 
# то ее заменить на перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.

my_list = ["wer", "qwe", "hpm", "jky"]
new_list = [value[::-1] if counter % 2 != 0 else value for counter, 
            value in enumerate(my_list)]
print(new_list)

#########################################################################

# 2. Дан список строк my_list. Создать новый список в который 
# поместить элементы из my_list у которых первый символ - буква "a".

my_list = ["dog", "anaconda", "cat", "alligator"]
# Генераторное выражение:
my_list_2 = [value for value in my_list if value [0] == 'a']
print(my_list_2)

#########################################################################

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ["dog", "anaconda", "cat", "alligator"]
my_list_2 = [my_list_2 for my_list_2 in my_list if 'a' in my_list_2]
print(my_list_2)

#########################################################################

# 4. Дан список my_list в котором могум быть как строки (type str) так и 
# целые числа (type int). Создать новый список в который поместить только 
# строки из my_list.

my_list = ["abc", 123, "def", 456]
my_list_2 = [symbol for symbol in my_list if isinstance(symbol, str)]
print(my_list_2)

#########################################################################

# 5. Дана строка my_str. Создать список в который поместить те символы из 
# my_str, которые встречаются в строке только один раз.

my_str = 'bottom'
my_list = list(set(my_str))
print(my_list)

#########################################################################

# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str = 'animal'
my_str_2 = 'human'
my_list = list(set(my_str)&set(my_str_2))
print(my_list)

#########################################################################

# 7. Даны две строки. Создать список в который поместить те символы, 
# которые есть в обеих строках, но в каждой только по одному разу.

my_str = 'animal'
my_str_2 = 'human'
my_list = []
for symbol in my_str:
    letter = my_str.find(symbol) - my_str.rfind(symbol)
    if letter == 0:
        if symbol in my_str_2 \
        and my_str_2.find(symbol) - my_str_2.rfind(symbol) == 0:
            my_list.append(symbol)
print(my_list)
            
###########################################################################

# 8. Описать с помощью словаря следующую структуру для конкретного человека 
# (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность
    
person = {"l_name": "Musk",
          "f_name": "Elon",
          "age": 49,
          "country": "USA",
          "city": "Los Angeles",
          "neighborhood ": "Bel Air",
          "job": "engineer",
          "net worth": "increase US$ 153.5 billion (December 2020)",
          "title": "product architect of Tesla"
          }
print(person["f_name"], person["l_name"], person["title"])

#############################################################################

# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
    
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло
    
print("Napoleon cake ingredients:")

cake_napoleon = {"flour in grams": 640,
                 "milk in liters": 1,
                 "margarine in grams": 400,
                 "eggs in pieces": 2,
                 }
print("cake layer:%s" % str (cake_napoleon))

cake_napoleon = {"sugar in grams": 175,
                 "butter in grams": 200,
                 "vanilla bags": 1,
                 "sour cream in grams": 0,
                 }
print("cream:%s" % str (cake_napoleon))

cake_napoleon = {"cacao in grams": 0,
                 "sugar in grams": 0,
                 "butter in grams": 0,
                 }
print("glaze:%s" % str (cake_napoleon))   






    
    
    
    
    
    
    
    
    
    
    
    
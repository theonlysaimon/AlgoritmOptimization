import json
import string
import os 
from test_module import *

while exit:
#загрузка dataset
    while True:
        try:
            print("Введите путь к файлу:    ")
            path = input()        
            path = path.replace('\\','/')
            
            with open(path, "r", encoding="utf8") as read_file:
                ng_1_data = json.load(read_file)
            break
        except ValueError:
            print("Ошибка значения")
        except IOError:
            print("Файл не найден")

    with open ("data/stop_ru.txt", 'r', encoding="utf8") as stop_file:
        rus_stops = [word.strip() for word in stop_file.readlines()] 

    while True:
        try:
            print("Введите количество прогоняемых кластеров:    ")

            clast = int(input())
            for item in ng_1_data[:clast]:
                print ('Эталонные ключевые слова: ', item['title'])
                print ('Самые частотные слова: ',  keywords_most_frequent_with_stop_and_lemm (item['news'][1]['body'], 6, rus_stops))
                print ("")
            break
        except ValueError:
            print("Неверное значение")  

    print("Работа завершена")
    while True:
        try:
            print("Желаете продолжить? y/n")
            exitpool = input()
            if exitpool == 'n':
                exit = False
                break
            elif exitpool == 'y':
                exit = True
                break
            elif exitpool != 'n' or exitpool != 'y':
                print("Неверный ввод")
        except ValueError:
            print("Введите y или n")
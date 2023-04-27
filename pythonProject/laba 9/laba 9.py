# 9.1)обработать любой операцией все картинки в заданной папке, используя для обхода файлов в папке модуль os (или Pathlib). При этом каталог для итоговых
# (обработанных) изображений должен тоже создаваться с помощью модуля os или Pathlib.

# 9.2) Модифицировать программу из практики 9.1, добавив проверку типа (расширения) файла, если в папке хранятся разные типы
# файлов, а вам нужно обработать только заданные (jpg, png).

# 9.3) Имеется файл с данными в формате csv:
# Продукт,Количество,Цена
# Молоко,2,80
# Сыр,1,500
# Хлеб,2,70

# Напишите программу, которая считывает данные из этого файла, подсчитывает итоговую сумму расходов и выводит данные в виде:
# Нужно купить:
# Молоко - 2 шт. за 80 руб.
# Сыр - 1 шт. за 500 руб.
# Хлеб - 2 шт. за 70 руб.
# Итоговая сумма: 800 руб.
import os
import glob
from PIL import ImageFilter, Image
os.chdir("9.1")
a=os.getcwd() #сохраняет текущий рабочий каталог
if not os.path.isdir("new"):#существует ли каталог с именем "new"
    os.mkdir("new") #Если это не так, он создает его с помощью функции os.mkdir.
for img in glob.glob('*.jpg'):#проходится по всем файлам .jpg в текущем рабочем каталоге, используя функцию glob.glob.
     with Image.open(img) as im:
         im.load()
         filter_ = im.filter(ImageFilter.FIND_EDGES)
         os.chdir("new") #Текущий рабочий каталог изменяется на новый каталог
         filter_.save("new_" + img) #сохраняет обработанное изображение в "новый" каталог с именем файла
         os.chdir(a)

def z3():
    import csv
    b='Нужно купить:\n'
    check=0
    with open('fail.csv', encoding='utf-8') as per:
        reader= csv.reader(per)
        zagolovok = next(per)#пропускает строку заголовка CSV-файла
        for row in reader:
            b = b+row[0]+' - '+row[1]+ ' шт. за '+ row[2] + ' руб.\n'
            check+=int(row[2])
    print(b+'Итоговая сумма = ', check, ' руб' )

z3()
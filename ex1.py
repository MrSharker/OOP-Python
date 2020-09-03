def prog():
    s = []
    print("Введите количество вещественных чисел")
    n = int(input())    #Определение количества чисел в списке
    while n != 0:
        print("Введите вещественное число: ")
        s.append(float(input()) * 0.13)
        n -= 1
    s.sort()            #Сортировка списка
    print("Готовый список: ")
    printl(s)           #Вывод списка на экран
    print("Сохранить список в файле?\n1.Да\n2.Нет")
    n = int(input())
    if n == 1:
        fileSave(s)     #Вызов функции сохранения данных в файле

def printl(s):          #Вывод элементов списка на экран с округлением до 2 знаков
    for i in s:
        print("%.2f" % i)

def fileSave(s):        #Сохранение данных списка в txt-файл в директории, где находится данный код
    with open("output.txt", "w") as file:
        for i in s:
            file.write(str("{0:.2f}".format(i)) + '\n')

prog()                  #Запуск программы
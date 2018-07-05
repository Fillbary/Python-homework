# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

list1 = ["apple", "banana", "qivi"]
num = 1
for i in list1:
    print (str(num)+".{:>9}".format(i))
    num+=1

list1 = ["apple", "banana", "qivi"]
for n,i in enumerate(list1):
    print(str(n+1) + ".{:>9}".format(i))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list1 = ['a','b','c','d','e','f','g']
list2 = ['a','m','c','z','e','o','g']
for i in list1:
    for u in list2:
        if i == u:
            list1.remove(i)
print (list1)

list1 = ['a','b','c','d','e','f','g']
list2 = ['a','m','c','z','e','o','g']
i=0
while i < len(list1):
    if list1[i] in list2:
        list1.pop(i)
        i+=1
print (list1)
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
import random
list1=[]
for i in range(20):
    list1.append(random.randint(-10,10))
print(list1)
list2=[]
for x in list1:
    if x%2 == 0:
        x = x / 4
        list2.append(x)
    else:
        x = x * 2
        list2.append(x)
print(list2)



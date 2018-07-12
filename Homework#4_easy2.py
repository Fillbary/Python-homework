# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list_l = ['banana', 'orange', 'apple', 'melon']
list_m = ['qiwi', 'banana', 'cucumber', 'pineapple', 'apple']
list_t = list (set (list_l) & set (list_m))
print(list_t)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random
import re
 
num = (random.randint(0, 9) for _ in range(2500)) 
str = ''.join(str(i) for i in num)
f = open("text.txt","w") 
f.write(str)
pattern = "[0]+"
result = re.findall(pattern,str)
print (result)
f.close()  

# #create
# a = 'привет' # Одинарные кавычки
# b = "привет" # Двойные кавычки
# c = "я'знаю'Python" # Комбинированные кавычки
# d = 'я"знаю"Python' # Можно и так
# e = 'я"знаю'Python" # А так нельзя (кавычки вперемешку)
# a = 123 # Целочисленный тип
# a = str(a) # Результат,'123'
# str([1,1.1,'a']) # Результат,"([1,1.1,'a'])"
# str(True) # Результат,'True'
# str(None) # Результат, 'None'
# #retrive
# a = 'привет'
# b = 'Иван'
# c = f"{a} я {b}" #"привет я Иван"
# a = ''
# print(a)
# print('Иван')
# a ='привет'
# a[0] # 'п'
# a[1] # 'р'
# a[2] # 'и'
# a[3] # 'в'
# a[4] # 'е'
# a[5] # 'т'
# a[6] # Ошибка,вышли за границы
# a[-1] # 'т'
# a[-2] # 'е'
# a[-3] # 'в'
# a[-4] # 'и'
# a[-5] # 'р'
# a[-6] # 'п'
# a[-7] # Ошибка,вышли за границы
# #del
# a = 'привет'
# a[0] 'б' #Хотели получить 'бривет',а получили ошибку,что строку нельзя изменять TypeError: 'str' object doesn't support item deletion
# a = 'бривет' # Для изменения придется полностью присвоить новое значение
# a = 'привет'
# del a[0] # ,TypeError: 'str' object doesn't support item deletion
# del a # Полное удаление переменной "a"



print(f'ЗАДАЧА 1')
lenght = 90
width = 50
perimeter = 2*(90+50)
print(perimeter)

print(f'ЗАДАЧА 2')
money = 10000
add = 10000+5000
print(add)

print(f'ЗАДАЧА 3')
hours = 5000
days = 5000//24
hour_1 = hours % days
print(days)
print(hour_1)

print('ЗАДАЧА 4')
pages = 100
lines = 50
symbol = 25
symbol_1 = 4
volume = 1.44 * 1024 * 1024
book = symbol_1 * symbol * lines * pages
book_2 = volume // book

print(book_2)

print(f'ЗАДАЧА 5')
r = 5
pi = 3.1415
side = 5
circle = 2 * pi * r
p = 4 * side
square = side ** 2
sq_circle = pi * (r ** 2)
print(f'{circle:.2f}')
print(square)
print(p)
print(f'{sq_circle:.2f}')

print(f'ЗАДАЧА 6')
str_numbers = 20 * '0' = 50 * '1' + 30 * '2'
print(str_numbers)

#1

a = 3
b = 8
def print_max(a, b):
    if a > b:
        print(a)
    else:
        print(b)

print_max(a, b)

#2

def check_number(a, b):
    if abs(a - b) == 135:
#пользовательская функция check_number проверяет разницу между числами (abs возвращает модуль числа)
        print "yes"
    else:
        print "no"
    

#3

def season(month):
    if month == 1 or month == 2 or month == 12:
        print ('зима')
    elif month == 3 or month == 4 or month == 5:
        print ('весна')
    elif month == 6 or month == 7 or month == 8:
        print ('лето')
    elif month == 9 or month == 10 or month == 11:
        print ('осень')
    else:
        print('Неверный номер')

season(13)
#номера месяцев для сокращения можно еще сделать через <= #

#4

def numbers_check(a, b, c):
#пользовательская функция numbers_check
    if a > 10 and b > 10 and c > 10:
        return "yes"
    else:
        return "no"

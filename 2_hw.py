def task_1() -> None:
    integer = 99
    print("Тип integer: (type(integer))")

    float = 7.62
    print("Тип float: (type(float))")

    string = "Привет"
    print("Тип string: (type(string))")

    list = [1, "три", 7.7, False]
    print("Тип list: (type(list))")

    boolean = False
    print("Тип boolean: (type(boolean))")

task_1()

#2#

def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3])
task_2()
#Последовательность Фибоначчи#


#3#


def task_3(number: float) -> float:
    return number ** 2
#тип данных float, так как исходное число может быть не целое.
A = task_3(5.7)
print(f"Квадрат числа равен: {A}")

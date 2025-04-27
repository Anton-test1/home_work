#1

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # расчет площади
        print(self.width * self.height)

    def perimeter(self):
        # расчет периметра
        print(2 * (self.width + self.height))


# Создаем три прямоугольника
r1 = Rectangle(7, 9)
r2 = Rectangle(5, 12)
r3 = Rectangle(3, 5)

print(f"Прямоугольник 1")
print(f"Площадь {r1.area()}")
print(f"Периметр {r1.perimeter()}\n")

print(f"Прямоугольник 2")
print(f"Площадь {r2.area()}")
print(f"Периметр {r2.perimeter()}\n")

print(f"Прямоугольник 3")
print(f"Площадь {r3.area()}")
print(f"Периметр {r3.perimeter()}\n")

#2

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
       #Добавляем условие для деления на 0
        if self.b != 0:
            print(self.a / self.b)
        else:
            print("На ноль делить нельзя")

    def subtraction(self):
        print(self.a - self.b)
       #Тест 

test = Math(15,5)
print('Сложение:')
test.addition()

print('Умножение:')
test.multiplication()

print('Деление:')
test.division()

print('Вычитание:')
test.subtraction()

#3

class PanelButton:
    def __init__(self, text):
        self.text = text
        self.type = 'Кнопка'
        self.locator = ''
#type- константа,а locator не указываем из условий
    def click(self):
        print (f'Клик по кнопке {self.text}')

text_box_button = PanelButton('Text Box')
check_box_button = PanelButton('Check Box')
radio_button_button = PanelButton('Radio Button')
web_tables_button = PanelButton('Web Tables')
buttons_button = PanelButton('Buttons')
links_button = PanelButton('Links')
broken_links_button = PanelButton('Broken Links - Images')
upload_download_button = PanelButton('Upload and Download')
dynamic_properties_button = PanelButton('Dynamic Properties')

buttons = [text_box_button, check_box_button, radio_button_button,
    web_tables_button, buttons_button, links_button,
    broken_links_button, upload_download_button, dynamic_properties_button]

for button in buttons:
    print(f'Текст кнопки: {button.text}')

for button in buttons:
    button.click()

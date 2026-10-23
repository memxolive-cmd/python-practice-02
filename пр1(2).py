#Конвертер единиц
print("Конвертер единиц")
print("1. Градус Цельсия -> Градус Фаренгейта")
print("2. Километры -> Мили")
print("3. Килограммы -> Фунты")
print("4. Метры -> Футы")

choice = input("Ваш выбор: ")

try:
    value = float(input("Введите значение: "))
except ValueError:
    print("Ошибка: введите число")
    exit()

if choice == '1':
    result = value * 9 / 5 + 32
    print(f"{value} C = {result} F")
elif choice == '2':
    result = value * 0.621371
    print(f"{value} км = {result} миль")
elif choice == '3':
    result = value * 2.20462
    print(f"{value} кг = {result} фунтов")
elif choice == '4':
    result = value * 3.28084
    print(f"{value} м = {result} футов")
else:
    print("Ошибка: неизвестный номер преобразования")
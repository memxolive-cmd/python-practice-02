#Консольный калькулятор
print("Консольный калькулятор")

try:
    a = float(input("Введите первое число: "))
except ValueError:
    print("Ошибка: это не число")
    exit()

op = input("Введите операцию (+, -, *, /, //, %, ^): ")

try:
    b = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка: это не число")
    exit()

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    if b == 0:
        print("Ошибка: деление на ноль")
        exit()
    result = a / b
elif op == '//':
    if b == 0:
        print("Ошибка: деление на ноль")
        exit()
    result = a // b
elif op == '%':
    if b == 0:
        print("Ошибка: деление на ноль")
        exit()
    result = a % b
elif op == '^':
    result = a ** b
else:
    print("Ошибка: неизвестная операция")
    exit()

print("Результат:", result)
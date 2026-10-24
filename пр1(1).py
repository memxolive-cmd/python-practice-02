print("Консольный калькулятор")

while True:
    # Ввод первого числа
    try:
        a = float(input("Введите первое число: "))
    except ValueError:
        print("Ошибка: это не число. Попробуйте снова.")
        continue
    
    op = input("Введите операцию (+, -, *, /, //, %, ^): ")
    
    # Проверка операции
    if op not in ('+', '-', '*', '/', '//', '%', '^'):
        print("Ошибка: неизвестная операция. Попробуйте снова.")
        continue
    
    # Ввод второго числа
    try:
        b = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: это не число. Попробуйте снова.")
        continue
    
    # Выполнение операции
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            print("Ошибка: деление на ноль. Попробуйте снова.")
            continue
        result = a / b
    elif op == '//':
        if b == 0:
            print("Ошибка: деление на ноль. Попробуйте снова.")
            continue
        result = a // b
    elif op == '%':
        if b == 0:
            print("Ошибка: деление на ноль. Попробуйте снова.")
            continue
        result = a % b
    elif op == '^':
        result = a ** b
    
    print("Результат:", result)
    
    # Вопрос о продолжении
    while True:
        answer = input("Хотите выполнить ещё одну операцию? (да/нет): ").strip().lower()
        if answer in ('да', 'нет'):
            break
        print("Ошибка: введите 'да' или 'нет'.")
    
    if answer == 'нет':
        print("Работа программы завершена.")
        break
#Разработать консольную программу, анализирующую введённое пользователем
#целое число.
try:
    n = int(input("Введите число: "))
except ValueError:
    print("Ошибка: это не целое число")
    exit()

if n > 0:
    print("Положительное: да")
elif n < 0:
    print("Положительное: нет")
else:
    print("Число равно нулю")


if n % 2 == 0:
    print("Четное: да")
else:
    print("Четное: нет")


if n % 3 == 0:
    print("Делится на 3: да")
else:
    print("Делится на 3: нет")

if n % 5 == 0:
    print("Делится на 5: да")
else:
    print("Делится на 5: нет")


if n < 2:
    print("Простое: нет")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Простое: да")
    else:
        print("Простое: нет")

print("Количество цифр:", len(str(abs(n))))
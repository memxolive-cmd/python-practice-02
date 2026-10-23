#Расчёт стоимости покупки
name = input("Товар: ")

try:
    price = float(input("Цена: "))
    quantity = int(input("Количество: "))
except ValueError:
    print("Ошибка: цена и количество должны быть числами")
    exit()

total = price * quantity
print("Итого:", total)

if total >= 15000:
    discount_percent = 15
elif total >= 10000:
    discount_percent = 10
elif total >= 5000:
    discount_percent = 5
else:
    discount_percent = 0

discount_rub = total * discount_percent / 100
final = total - discount_rub

print("Скидка в процентах:", discount_percent, "%")
print("Скидка в рублях:", discount_rub)
print("Итоговая цена:", final)
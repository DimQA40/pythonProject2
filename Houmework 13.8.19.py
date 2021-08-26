tickets = int(input("Введите количество приобретаемых билетов - "))
payment_sum = 0

for visitor in range(1,tickets+1):
    age_visitor = int(input("Введите возраст постетителя: "))
    if age_visitor < 18:
        payment_sum +=0
    elif 18 <= age_visitor < 25:
        payment_sum += 990
    elif age_visitor >= 25:
        payment_sum += 1390
if tickets > 3:
    payment_sum = payment_sum - (payment_sum * 10 / 100)
    print("Скидка составила: ", round(payment_sum * 10 / 100))
print("Общая стоимость билетов составляет : ", payment_sum)

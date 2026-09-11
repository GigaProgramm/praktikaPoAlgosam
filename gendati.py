from datetime import datetime, timedelta, date
import random

# проверяет даты на корректность
# выводит массив с корректными датами 
def check_dates(*dates):
    result = []
    for current_date in dates:
        try: 
            datetime.strptime(current_date, "%Y-%m-%d") # strptime нужна для парсинга строки в дату
            result.append(current_date)
        except ValueError:
            pass
    return result

# функция генерирует даты через дельту дат
# принимает кол-во генерируемых дат 
# выводит массив с датами 
def generate_dates(count): # работает с кол-вом дат
    start_date = date(2000, 1, 31) # начальная дата
    end_date = date(2050, 1, 31) # конечная дата
    delta = end_date - start_date # дельта дат

    result = []

    if delta.day <= 0:
        print ("Не корректный диапазон дат!")
        return []
    for i in range (count):
        random_day = random.randint(0, delta.days)
        result.append((start_date + timedelta(days=random_day)).strftime("%Y-%m-%d")) 
        print((start_date + timedelta(days=random_day)).strftime("%Y-%m-%d"))

    return result

try:
    count_dates = int(input("Введите кол-во дат: "))
    result_dates = check_dates(*generate_dates(count_dates)) # генерация и проверка массива дат
except ValueError:
    print("Ошибка! Введите корректные данные") 

print("Сгенерированные даты: ")
for i in result_dates:
    print(i)

# вывод результата
print(f"Количество корректных дат: {len(result_dates)}")
print(f"Самая ранняя дата: {max(result_dates)}")
print(f"Самая поздняя дата: {min(result_dates)}")
print(f"Список будущих дат относительно сегодняшнего дня({datetime.now().date()}): ")
# вывод дат после нынешней
result_dates.sort()
for i in result_dates:
    if datetime.strptime(i, "%Y-%m-%d").date() > datetime.now().date():
        print(i)

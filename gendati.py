from datetime import datetime, timedelta, date
import random


# проверяет даты на корректность
# выводит массив с корректными датами
def check_dates(*dates):
    valid_dates = []
    for current_date in dates:
        try:
            datetime.strptime(current_date, "%Y-%m-%d")
            valid_dates.append(current_date)
        except ValueError:
            continue

    valid_dates.sort()
    today = datetime.now().date()
    future_dates = [
        d for d in valid_dates
        if datetime.strptime(d, "%Y-%m-%d").date() > today
    ]

    return {
        "valid_dates": valid_dates,
        "count": len(valid_dates),
        "earliest": valid_dates[0] if valid_dates else None,
        "latest": valid_dates[-1] if valid_dates else None,
        "future_dates": future_dates,
    }


# функция генерирует даты через дельту дат
# принимает кол-во генерируемых дат
# выводит массив с датами
def generate_dates(count, down_br, up_br):  # работает с кол-вом дат
    start_date = date(int(down_br[0]), int(down_br[1]), int(down_br[2]))  # начальная дата
    end_date = date(int(up_br[0]), int(up_br[1]), int(up_br[2]))  # конечная дата
    delta = end_date - start_date  # дельта дат

    result = []

    for i in range(count):
        random_day = random.randint(0, delta.days)
        result.append((start_date + timedelta(days=random_day)).strftime("%Y-%m-%d"))

    return result


while True:
    try:
        down_border = input("Введите нижнюю границу генерации " \
        "дат(формата ГГГГ-ММ-ДД): ")

        up_border = input("Введите верхнюю границу генерации " \
        "дат(формата ГГГГ-ММ-ДД): ")

        date_down_border = datetime.strptime(down_border, "%Y-%m-%d")
        date_up_border = datetime.strptime(up_border, "%Y-%m-%d")

        count_dates = int(input("Введите кол-во дат: "))
        if count_dates <= 0:
            print("Введите кол-во дат больше 0!")
            continue

        if date_down_border > date_up_border: 
            print("Введите границы в правильной последовательности!")
            continue

        if date_down_border == date_up_border:
            print("Даты не должны быть одинаковыми!")
            continue

        result_dates = check_dates(
            *generate_dates(count_dates, down_border.split("-"), up_border.split("-"))
        )  # генерация и проверка массива дат
        break
    except ValueError:
        print("Ошибка! Введите корректные данные")

generated = generate_dates(count_dates, down_border.split("-"), up_border.split("-"))
report = check_dates(*generated)

print("Сгенерированные даты: ")
for i in result_dates:
    print(i)

# вывод результата
print(f"\nКорректные даты: {report['valid_dates']}")
print(f"Количество корректных дат: {report['count']}")
print(f"Самая ранняя дата: {report['earliest']}")
print(f"Самая поздняя дата: {report['latest']}")
print(f"Список будущих дат относительно сегодняшнего дня ({datetime.now().date()}):")
for d in report["future_dates"]:
    print(d)

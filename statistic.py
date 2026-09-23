# программа для расчёта статистических вычисдений

import statistics
import random as rd

# функция обработки статистических данных
# принимает на вход режим работы и обрабатываемый массив данных
# на выходе список с результатом
def stats_calculator(*args, mode="basic"):
    # обработка отсутсвия данных

    if not args:
        return "Нет данных"

    result = {}

    # базовый режим и все остальные типа
    result["Минимум"] = min(args)
    result["Максимум"] = max(args)
    result["Среднее арифметическое"] = statistics.mean(args)

    # для режима адвансед и сиентифик
    if mode in ["advanced", "scientific"]:
        result["Медиана"] = statistics.median(args)
        try:
            result["Мода"] = statistics.mode(
                args
            )  # в новых версиях питона statistics.mode не выдаёт ощибки при отстутсвии моды
        except statistics.StatisticsError:
            result["Мода"] = None
    # только для сиентифик
    if mode in ["scientific"]:
        # обработчик ошибок от модуля статистикс 
        try:
            result["Среднее геометрическое"] = statistics.geometric_mean(args)
        except statistics.StatisticsError:
            result["Среднее геометрическое"] = None
        try:
            result["Среднее гармоническое"] = statistics.harmonic_mean(args)
        except statistics.StatisticsError:
            result["Среднее гармоническое"] = None

    return result


while True:
    try:
        # ввод данных от пользователя
        down_border = int(input("Введите нижнюю границу генерации(больше 0): "))
        up_border = int(input("Введите верхнюю границу генерации: "))
        mode_input = input("Введите режим(basic, advanced, scientific): ").strip().lower()
        count_num = int(input("Введите кол-во генерируемых чисел: "))
        if count_num < 0:
            print("Кол-во чисел должно быть больше нуля")
            continue
        if up_border < down_border:
            print("Введите границы генерации корректно")
            continue
        if down_border < 0:
            print("Введите нижнюю границу генерации больше 0")
            continue
        break
    except ValueError:
        print("Ошибка! Введите корректные данные")

# обработка не правильных данных
if mode_input not in ["basic", "advanced", "scientific"]:
    print(f"Не верный ввод режима({mode_input}), использую basic")
    mode_input = "basic"
# генерируем числа от down_border до up_border
random_number = [
    rd.randint(down_border, up_border) for _ in range(count_num)
]  # генерируем массив с рандомными числами через списковое включение

stats = stats_calculator(*random_number, mode=mode_input)

# вывод результата
print(f"Сгенерированный массив: {random_number}\n")
print(f"Выбранный режим: {mode_input}\n")
for key, value in stats.items():  # получаю ключ-значение через items()
    print(f"{key}: {value}")

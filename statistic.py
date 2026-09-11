# программа для расчёта статистических вычисдений

import statistics
import random as rd

MAX_NUMBER = 100 # максимальное число при генерации

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
            result["Мода"] = statistics.mode(args) # в новых версиях питона statistics.mode не выдаёт ощибки при отстутсвии моды
        except statistics.StatisticsError:
            result["Мода"] = None
    # только для сиентифик
    if mode in ["scientific"]:
        result["Среднее геометрическое"] = statistics.geometric_mean(args)
        result["Среднее гармоническое"] = statistics.harmonic_mean(args)

    return result

try:
    # ввод данных от пользователя
    mode_input = input("Введите режим(basic, advanced, scientific): ").strip().lower()
    count_num = int(input("Введите кол-во генерируемых чисел: "))
except ValueError:
    print("Ошибка! Введите корректные данные")

# обработка не правильных данных
if mode_input not in ["basic", "advanced", "scientific"]:
    mode_input = "basic"
# генерируем числа от 1 до MAX_NUMBER
random_number = [rd.randint(1, MAX_NUMBER) for _ in range(count_num)] # генерируем массив с рандомными числами через списковое включение

stats = stats_calculator(*random_number, mode=mode_input)

# вывод результата 
print(f"Сгенерированный массив: {random_number}\n")
print(f"Выбранный режим: {mode_input}\n")
for key, value in stats.items(): # получаю ключ-значение через items()
    print(f"{key}: {value}")


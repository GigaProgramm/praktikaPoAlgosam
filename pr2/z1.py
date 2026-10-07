
from functools import reduce

students = {
    "Артём": [2, 2, 2, 2],
    "Александр": [5, 5, 5, 5],
    "Николай": [3, 5, 4, 4],
    "Тимур": [3, 3, 5, 4],
    "Кирилл": [5, 4, 4, 5, 4, 3],
    "Михаил": [3, 5, 4, 3, 2]
}

# функция провверки данных
def validate_students(data):
    if not isinstance(data, dict) or not data:
        raise ValueError("Словарь студентов пуст или не является словарём")
    for name, marks in data.items():
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"Некорректное имя студента: {name!r}")
        if not isinstance(marks, list) or not marks:
            raise ValueError(f"У студента {name} нет оценок")
        for mark in marks:
            # bool - это подкласс int, поэтому его исключаем отдельно
            if not isinstance(mark, int) or isinstance(mark, bool) or not 2 <= mark <= 5:
                raise ValueError(f"У студента {name} некорректная оценка: {mark!r}")

# создаёт словарь с именем и средним баллом 
def get_average(data): 
    return dict(
        map(lambda item: (item[0], round(sum(item[1]) / len(item[1]), 2)), data.items())
    )

#сортировака по убыванию для балла
def sort_average(averages):
    # минус перед баллом разворачивает порядок для среднего,
    # а имя сортируется по алфавиту
    return dict(sorted(averages.items(), key=lambda item: (-item[1], item[0])))

# общее кол-во оценок у всей группы
def count_marks(data):
    return reduce(lambda total, marks: total + len(marks), data.values(), 0)

# студент с наибольшим разбросом
def max_spread_students(data):
    return max(data, key=lambda name: max(data[name]) - min(data[name]))

try:
    validate_students(students)
except ValueError as error:
    print(f"Ошибка в данных: {error}")
    exit()

averages = get_average(students)
print(f"Средние баллы: {averages}")
print(f"Отсортированные средние баллы: {sort_average(averages)}")
print(f"Всего оценок: {count_marks(students)}")
print(f"Наибольший разброс у: {max_spread_students(students)}")

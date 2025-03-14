import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "salaries.txt")


def total_salary(path: str) -> tuple:
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = [
                float(line.strip().split(",")[1]) for line in file if line.strip()
            ]

            if not salaries:  # Проверяем, есть ли данные
                return (0, 0)

        total_salary = sum(salaries)
        avg_salary = total_salary / len(salaries)

        return total_salary, avg_salary

    except FileNotFoundError:
        print(f"⚠️ Ошибка: Файл '{path}' не найден.")
        return (0, 0)


total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

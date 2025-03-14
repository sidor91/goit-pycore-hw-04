import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "cats_data.txt")


def get_cats_info(path: str) -> list:
    result = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    cats_info_list = line.strip().split(",")

                    if len(cats_info_list) == 3:
                        id, name, age = cats_info_list
                        try:
                            result.append({"id": id, "name": name, "age": int(age)})
                        except ValueError:
                            print(
                                f"⚠️ Ошибка: Неверный формат числа в строке '{line.strip()}'"
                            )
                    else:
                        print(
                            f"⚠️ Ошибка: Неправильное количество полей в строке '{line.strip()}'"
                        )

    except FileNotFoundError:
        print(f"⚠️ Ошибка: Файл '{path}' не найден.")
        return []
    except UnicodeDecodeError:
        print(f"⚠️ Ошибка: Файл '{path}' имеет неподдерживаемую кодировку.")
        return []
    except OSError:
        print(f"⚠️ Ошибка: Файл '{path}' поврежден или не может быть прочитан.")
        return []

    return result


print(get_cats_info(file_path))

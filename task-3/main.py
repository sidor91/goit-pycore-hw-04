import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def print_directory_tree(path: Path, indent=""):
    """Рекурсивно выводит структуру директорий."""
    try:
        if not path.exists():
            print(Fore.RED + f"Ошибка: Путь '{path}' не существует!")
            return
        if not path.is_dir():
            print(Fore.RED + f"Ошибка: '{path}' не является директорией!")
            return

        print(Fore.CYAN + f"Структура каталога: {path}\n")

        for item in path.iterdir():
            if item.is_dir():
                print(Fore.BLUE + f"{indent}📁 {item.name}/")
                print_directory_tree(item, indent + "    ")
            else:
                print(Fore.GREEN + f"{indent}📄 {item.name}")
    except Exception as e:
        print(Fore.RED + f"Ошибка: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Использование: python script.py /путь/к/директории")
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    print_directory_tree(directory_path)

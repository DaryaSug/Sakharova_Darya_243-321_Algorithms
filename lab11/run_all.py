from pathlib import Path
import runpy


# Значения идут в том же порядке, что и запросы input() в задании.
# Чтобы проверить другие данные, измените нужный список.
EXAMPLES = {
    '1.py': [7, 4, 2, 6, 1, 3, 5, 7],
}


def run_task(path, values):
    position = 0

    def example_input(prompt=""):
        nonlocal position
        if position >= len(values):
            raise ValueError("Не хватает готовых значений для ввода.")
        value = str(values[position])
        position += 1
        print(f"{prompt}{value}")
        return value

    # Запускаем исходное задание и подставляем значения вместо ручного ввода.
    runpy.run_path(str(path), init_globals={"input": example_input}, run_name="__main__")
    if position != len(values):
        raise ValueError("В списке есть лишние значения для ввода.")


def main():
    folder = Path(__file__).resolve().parent
    tasks = sorted(
        (path for path in folder.glob("*.py") if path.stem.isdigit()),
        key=lambda path: int(path.stem),
    )
    print(f"Лабораторная работа {folder.name.removeprefix('lab')}")
    errors = 0
    for path in tasks:
        print(f"\n--- Задание {path.stem} ({path.name}) ---")
        try:
            if path.name not in EXAMPLES:
                raise ValueError("Добавьте готовые значения для этого задания в EXAMPLES.")
            run_task(path, EXAMPLES[path.name])
        except Exception as error:
            print(f"Ошибка: {error}")
            errors += 1
    print(f"\nВсего заданий: {len(tasks)}. Ошибок: {errors}.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

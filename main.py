import os

from create_month_images import create_month_images_with_background_1

# Базовый год
base_year = {
    "Январь": {"Общий день": 2, "Личный день": 3},
    "Февраль": {"Общий день": 3, "Личный день": 4},
    "Март": {"Общий день": 4, "Личный день": 5},
    "Апрель": {"Общий день": 5, "Личный день": 6},
    "Май": {"Общий день": 6, "Личный день": 7},
    "Июнь": {"Общий день": 7, "Личный день": 8},
    "Июль": {"Общий день": 8, "Личный день": 9},
    "Август": {"Общий день": 9, "Личный день": 1},
    "Сентябрь": {"Общий день": 1, "Личный день": 2},
    "Октябрь": {"Общий день": 2, "Личный день": 3},
    "Ноябрь": {"Общий день": 3, "Личный день": 4},
    "Декабрь": {"Общий день": 4, "Личный день": 5},
}

# Создаем массив для 9 лет
start_numbers = []

for year in range(9):
    year_data = {}
    for month, values in base_year.items():
        # Сохраняем "Общий день" без изменений
        general_day = values["Общий день"]

        # "Личный день" сдвигается на 1 каждый год
        personal_day = (values["Личный день"] + year - 1) % 9 + 1  # Сдвиг по кругу от 1 до 9

        # Добавляем месяц с обновленными значениями
        year_data[month] = {"Общий день": general_day, "Личный день": personal_day}
    
    # Добавляем год в массив
    start_numbers.append(year_data)

def main():
    # Каталоги для шрифтов и изображений
    fonts_dir = "fonts"
    images_dir = "images"

    # Пути к файлам
    font_path = os.path.join(fonts_dir, "ofont.ru_Uncage.ttf")
    background_image = os.path.join(images_dir, "background.png")
    
    base_folder= "months_png/"
    # base_folder = "all_years/"


    # text_color = "black"
    text_color = (41, 7, 99)

    # Проверка существования каталогов
    if not os.path.exists(fonts_dir):
        print(f"Каталог с шрифтами не найден: {fonts_dir}")
        return

    if not os.path.exists(images_dir):
        print(f"Каталог с изображениями не найден: {images_dir}")
        return

    print("Генерация календарных изображений...")
    for i in range(9):
        output_folder = base_folder + str(i+1)
        create_month_images_with_background_1(output_folder, background_image, font_path, text_color, start_numbers[i])


if __name__ == "__main__":
    main()

from PIL import Image, ImageDraw, ImageFont
import calendar
import os

# Начальные числа для каждого месяца
# start_numbers = {
#     "Январь": {"Общий день": 2, "Личный день": 3},
#     "Февраль": {"Общий день": 3, "Личный день": 4},
#     "Март": {"Общий день": 4, "Личный день": 5},
#     "Апрель": {"Общий день": 5, "Личный день": 6},
#     "Май": {"Общий день": 6, "Личный день": 7},
#     "Июнь": {"Общий день": 7, "Личный день": 8},
#     "Июль": {"Общий день": 8, "Личный день": 9},
#     "Август": {"Общий день": 9, "Личный день": 1},
#     "Сентябрь": {"Общий день": 1, "Личный день": 2},
#     "Октябрь": {"Общий день": 2, "Личный день": 3},
#     "Ноябрь": {"Общий день": 3, "Личный день": 4},
#     "Декабрь": {"Общий день": 4, "Личный день": 5},
# }

def create_month_images_with_background_1(output_folder, background_image, font_path, text_color, start_numbers):
    """Создание изображений для каждого месяца с текстами в ячейках."""
    width, height = 3200, 1800
    os.makedirs(output_folder, exist_ok=True)

    if not os.path.exists(font_path):
        print(f"Файл шрифта {font_path} не найден!")
        return

    font_title = ImageFont.truetype(font_path, 100)
    font_day = ImageFont.truetype(font_path, 45)
    font_date = ImageFont.truetype(font_path, 35)
    font_cell_text = ImageFont.truetype(font_path, 25)

    if not os.path.exists(background_image):
        print(f"Файл фона {background_image} не найден!")
        return
    bg = Image.open(background_image).resize((width, height))

    days_ru = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    months_ru = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                 "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

    cell_width, cell_height = 400, 200
    padding = 10
    total_grid_width = len(days_ru) * (cell_width + padding) - padding
    start_x = (width - total_grid_width) // 2

    highlight_color_3 = (132, 171, 172, 150)  # Зелёный цвет
    highlight_color_6 = (72, 93, 129, 150)  # Синий цвет
    highlight_color_date = (125, 83, 113, 150)  # Малиновый для 10, 20, 30 чисел
    default_color = (200, 200, 200, 150)  # Обычный цвет ячеек

    for month in range(1, 13):
        img = bg.copy()
        draw = ImageDraw.Draw(img, "RGBA")

        month_name = months_ru[month - 1].upper()
        text_width = draw.textlength(month_name, font=font_title)
        draw.text(((width - text_width) // 2, 60), month_name, fill=text_color, font=font_title)
        draw.text((width // 2 - 50, 200), "2025", fill="black", font=font_day)

        # Начальные числа для текущего месяца
        general_day_number = start_numbers[months_ru[month - 1]]["Общий день"]
        personal_day_number = start_numbers[months_ru[month - 1]]["Личный день"]

        start_y = 300
        for i, day in enumerate(days_ru):
            x = start_x + i * (cell_width + padding)
            y = start_y
            draw.rectangle([x, y, x + cell_width, y + cell_height], fill=(50, 50, 50, 180), outline=None)

            text_width = draw.textlength(day, font=font_day)
            draw.text((x + (cell_width - text_width) // 2, y + 60), day, fill="white", font=font_day)

        cal = calendar.monthcalendar(2025, month)
        for week_idx, week in enumerate(cal):
            for day_idx, day in enumerate(week):
                x1 = start_x + day_idx * (cell_width + padding)
                y1 = start_y + (week_idx + 1) * (cell_height + padding)
                x2 = x1 + cell_width
                y2 = y1 + cell_height

                # Определяем цвет ячейки
                if day:
                    if day in [10, 20, 30]:  # Если день — 10, 20 или 30, приоритет малиновый
                        cell_color = highlight_color_date
                    elif general_day_number == 3:  # Зелёный цвет
                        cell_color = highlight_color_3
                    elif general_day_number == 6:  # Синий цвет
                        cell_color = highlight_color_6
                    else:
                        cell_color = default_color

                    draw.rectangle([x1, y1, x2, y2], fill=cell_color, outline=None)

                    draw.text((x1 + 20, y1 + 20), str(day), fill="black", font=font_date)
                    
                    # Добавление текста "Личный день - цифра"
                    personal_text = f"Личный день - {personal_day_number}"
                    personal_width = draw.textlength(personal_text, font=font_cell_text)
                    draw.text((x1 + (cell_width - personal_width) // 2, y1 + 60), 
                              personal_text, fill="black", font=font_cell_text)
                    
                    # Добавление текста "Общий день - цифра"
                    general_text = f"Общий день - {general_day_number}"
                    general_width = draw.textlength(general_text, font=font_cell_text)
                    draw.text((x1 + (cell_width - general_width) // 2, y1 + 140), 
                              general_text, fill="black", font=font_cell_text)
                    
                    # Независимое обновление day_number
                    general_day_number = 1 if general_day_number == 9 else general_day_number + 1
                    personal_day_number = 1 if personal_day_number == 9 else personal_day_number + 1

        # Формирование имени файла
        file_index = 18 + month - 1
        image_path = os.path.join(output_folder, f"{file_index:03d}-2.png")
        img.save(image_path, "PNG")
        print(f"Сохранено: {image_path}")

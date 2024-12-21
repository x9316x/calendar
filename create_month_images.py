from PIL import Image, ImageDraw, ImageFont
import calendar
import os

def create_month_images_with_background(output_folder, background_image, font_path):
    """Создание изображений для каждого месяца."""
    width, height = 3200, 1800
    os.makedirs(output_folder, exist_ok=True)

    if not os.path.exists(font_path):
        print(f"Файл шрифта {font_path} не найден!")
        return

    font_title = ImageFont.truetype(font_path, 100)
    font_day = ImageFont.truetype(font_path, 45)
    font_date = ImageFont.truetype(font_path, 35)

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

    for month in range(1, 13):
        img = bg.copy()
        draw = ImageDraw.Draw(img, "RGBA")

        month_name = months_ru[month - 1].upper()
        text_width = draw.textlength(month_name, font=font_title)
        draw.text(((width - text_width) // 2, 60), month_name, fill="black", font=font_title)
        draw.text((width // 2 - 50, 200), "2025", fill="black", font=font_day)

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
                color = (255, 255, 255, 0) if not day else (200, 200, 200, 150)
                draw.rectangle([x1, y1, x2, y2], fill=color, outline=None)
                if day:
                    draw.text((x1 + 20, y1 + 20), str(day), fill="black", font=font_date)

        image_path = os.path.join(output_folder, f"{month:02d}_{months_ru[month - 1]}.png")
        img.save(image_path, "PNG")
        print(f"Сохранено: {image_path}")

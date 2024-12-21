from PIL import Image, ImageDraw, ImageFont
import os

def create_ganeral_image_2(output_folder, background_image, font_path):
    """Создание титульного изображения."""
    width, height = 3200, 1800
    title_image_path = os.path.join(output_folder, "0011_Общий.png")

    if not os.path.exists(font_path):
        print(f"Файл шрифта {font_path} не найден!")
        return

    font_title = ImageFont.truetype(font_path, 150)
    font_subtitle = ImageFont.truetype(font_path, 80)

    if not os.path.exists(background_image):
        print(f"Файл фона {background_image} не найден!")
        return
    bg = Image.open(background_image).resize((width, height))
    draw = ImageDraw.Draw(bg)

    # Заголовок
    title_text = "2025"

    # Две строки подзаголовка
    subtitle_lines = [
        "ВСЕ СИСТЕМЫ И ПРАВИЛА, ПО КОТОРЫМ МЫ ЖИЛИ РАНЬШЕ,", 
        "ПОМЕНЯЮТСЯ НА КАРДИНАЛЬНО НОВЫЕ"
    ]

    # Отрисовка заголовка
    text_width = draw.textlength(title_text, font=font_title)
    draw.text(((width - text_width) // 2, 600), title_text, fill="black", font=font_title)

    # Отрисовка каждой строки подзаголовка
    start_y = 800  # Начальная позиция Y для подзаголовка
    line_spacing = 100  # Расстояние между строками

    for i, line in enumerate(subtitle_lines):
        text_width = draw.textlength(line, font=font_subtitle)
        draw.text(((width - text_width) // 2, start_y + i * line_spacing), line, fill="black", font=font_subtitle)



    bg.save(title_image_path, "PNG")
    print(f"Титульный слайд сохранён как {title_image_path}")


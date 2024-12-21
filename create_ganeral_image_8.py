from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def create_ganeral_image_8(output_folder, background_image, font_path, text_color):
    """Создание слайда с плюсом и минусом."""
    width, height = 3200, 1800
    title_image_path = os.path.join(output_folder, "008_Общий.png")

    if not os.path.exists(font_path):
        print(f"Файл шрифта {font_path} не найден!")
        return

    font_title = ImageFont.truetype(font_path, 150)
    font_text = ImageFont.truetype(font_path, 50)

    if not os.path.exists(background_image):
        print(f"Файл фона {background_image} не найден!")
        return
    bg = Image.open(background_image).resize((width, height))
    draw = ImageDraw.Draw(bg)

    # Заголовок
    title_text = "2025"
    title_width = draw.textlength(title_text, font=font_title)
    draw.text(((width - title_width) // 2, 200), title_text, fill=text_color, font=font_title)

    # Текст "В плюсе" и его содержание
    plus_title = "В ПЛЮСЕ:"
    plus_text = (
        "Когда к человеку приходит год Солнца, человеку предстоит открыть новое дело."
        "Решимость, уверенность в себе. Видение своего пути, масштаб. Способность вести за собой."
    )

    # Текст "В минусе" и его содержание
    minus_title = "В МИНУСЕ:"
    minus_text = (
        "Происходит снижение сердечной чакры, сжатие в груди."
        "Неудовлетворенность собой, нереализованный потенциал. Эгоизм, агрессия, деспотизм."

    )

    # Координаты текста
    left_margin = 100
    right_margin = width // 2 + 50
    text_start_y = 500
    line_spacing = 25  # Отступ между строками

    # Вывод текста "В плюсе"
    draw.text((left_margin, text_start_y), plus_title, fill="green", font=font_text)
    current_y = text_start_y + 70
    wrapped_plus_text = textwrap.fill(plus_text, width=40)
    for line in wrapped_plus_text.split('\n'):
        draw.text((left_margin, current_y), line, fill=text_color, font=font_text)
        current_y += font_text.size + line_spacing

    # Вывод текста "В минусе"
    draw.text((right_margin, text_start_y), minus_title, fill="red", font=font_text)
    current_y = text_start_y + 70
    wrapped_minus_text = textwrap.fill(minus_text, width=40)
    for line in wrapped_minus_text.split('\n'):
        draw.text((right_margin, current_y), line, fill=text_color, font=font_text)
        current_y += font_text.size + line_spacing

    # Сохранение изображения
    bg.save(title_image_path, "PNG")
    print(f"Восьмой слайд сохранён как {title_image_path}")

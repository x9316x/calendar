from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def create_ganeral_image_7(output_folder, background_image, font_path):
    """Создание слайда с заголовком и текстом."""
    width, height = 3200, 1800
    output_path = os.path.join(output_folder, "007_Общий.png")  # Имя выходного файла

    if not os.path.exists(font_path):
        print(f"Файл шрифта {font_path} не найден!")
        return

    font_title = ImageFont.truetype(font_path, 100)  # Шрифт заголовка
    font_text = ImageFont.truetype(font_path, 50)  # Шрифт текста

    if not os.path.exists(background_image):
        print(f"Файл фона {background_image} не найден!")
        return
    bg = Image.open(background_image).resize((width, height))
    draw = ImageDraw.Draw(bg)

    # Заголовок
    title_text = "ГОД 1 - СОЛНЦА. НАЧАЛО ВСЕГО НОВОГО"
    title_x = (width - draw.textlength(title_text, font=font_title)) // 2
    draw.text((title_x, 200), title_text, fill="black", font=font_title)

    # Основной текст
    main_text = (
        "Это время, когда нужно готовиться к переменам. В этом году происходит восстановление и прилив энергии. "
        "В жизнь приходит вдохновение для начала чего-то нового. Желательно придумывать новые идеи, размышлять о том, "
        "как бы Вы хотели прожить следующие девять лет. Год Солнца – это начало новой жизни, новый этап."
    )
    text_start_y = 400  # Начальная позиция Y для основного текста
    line_spacing = 20  # Расстояние между строками текста
    wrapped_text = textwrap.fill(main_text, width=70)  # Ширина текста

    # Рисуем текст по строкам
    for line in wrapped_text.split("\n"):
        line_x = (width - draw.textlength(line, font=font_text)) // 2
        draw.text((line_x, text_start_y), line, fill="black", font=font_text)
        text_start_y += font_text.size + line_spacing

    # Сохраняем результат
    bg.save(output_path, "PNG")
    print(f"Слайд сохранён как {output_path}")

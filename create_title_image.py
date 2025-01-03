from PIL import Image, ImageDraw, ImageFont
import os

def create_title_image(output_folder, background_image, font_path, text_color):
    """Создание титульного изображения."""
    width, height = 3200, 1800
    title_image_path = os.path.join(output_folder, "00_Титульный.png")

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

    # Добавляем текст
    title_text = "2025"
    subtitle_text = "КАЛЕНДАРЬ УСПЕХА"

    text_width = draw.textlength(title_text, font=font_title)
    draw.text(((width - text_width) // 2, 600), title_text, fill=text_color, font=font_title)

    text_width = draw.textlength(subtitle_text, font=font_subtitle)
    draw.text(((width - text_width) // 2, 800), subtitle_text, fill=text_color, font=font_subtitle)

    bg.save(title_image_path, "PNG")
    print(f"Титульный слайд сохранён как {title_image_path}")


from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def create_ganeral_image_4(output_folder, background_image, font_path):
    """Создание четвёртого слайда."""
    width, height = 3200, 1800
    title_image_path = os.path.join(output_folder, "0013_Общий.png")

    if not os.path.exists(font_path):
        print(f"Файл шрифта {font_path} не найден!")
        return

    font_title = ImageFont.truetype(font_path, 150)
    font_subtitle = ImageFont.truetype(font_path, 80)
    font_text = ImageFont.truetype(font_path, 50)

    if not os.path.exists(background_image):
        print(f"Файл фона {background_image} не найден!")
        return
    bg = Image.open(background_image).resize((width, height))
    draw = ImageDraw.Draw(bg)

    # Текст
    title_text = "2025"
    subtitle_text = "Год МАРСА Год СЛУЖЕНИЯ И ЗАВЕРШЕНИЯ ЦИКЛА"
    paragraph_text = (
        "2025 - год под энергией цифры 9. Это год подведения итогов и завершения начатых дел. Вы можете продолжать пожинать плоды своих стараний, "
        "как и в предыдущем году. Возможно завершение отношений, расставание с теми проектами, которые должны были "
        "закончиться. Это год очищения перед следующим началом нового цикла. Не надо тащить прошлое с собой в новый "
        "цикл. Год 9 существует для того, чтобы переосмыслить всё, что произошло за девять лет. Человек в этом году "
        "должен отбросить то, что ему уже не нужно, и забрать с собой все необходимое в следующий цикл. В этот год "
        "может разрушиться всё то, что создавалось до этого. Однако, в личный период – 9, к нам приходят различные "
        "идеи! И часто это идеи на миллиард."
    )

    # Позиция заголовка
    title_bbox = draw.textbbox((0, 0), title_text, font=font_title)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((width - title_width) // 2, 200), title_text, fill="black", font=font_title)

    # Позиция подзаголовка
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=font_subtitle)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    draw.text(((width - subtitle_width) // 2, 400), subtitle_text, fill="black", font=font_subtitle)

    # Перенос текста вручную и выравнивание по ширине и центру
    wrapped_lines = textwrap.fill(paragraph_text, width=75).split('\n')  # Разделяем на строки
    current_y = 600  # Начальная вертикальная позиция текста
    line_spacing = 15  # Отступ между строками

    for line in wrapped_lines:
        line_bbox = draw.textbbox((0, 0), line, font=font_text)
        line_width = line_bbox[2] - line_bbox[0]
        x_position = (width - line_width) // 2  # Центрируем каждую строку
        draw.text((x_position, current_y), line, fill="black", font=font_text)
        current_y += line_bbox[3] - line_bbox[1] + line_spacing  # Сдвигаем вниз для следующей строки

    # Сохранение изображения
    bg.save(title_image_path, "PNG")
    print(f"Четвёртый слайд сохранён как {title_image_path}")

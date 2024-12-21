from PIL import Image
import os

def personal_year_1(output_folder, background_image, phone_image_path):
    """Создание страницы с изображением телефона по центру."""
    width, height = 3200, 1800
    output_path = os.path.join(output_folder, "006_Общий.png")  # Имя выходного файла

    # Загружаем фон
    if not os.path.exists(background_image):
        print(f"Файл фона {background_image} не найден!")
        return
    bg = Image.open(background_image).resize((width, height))

    # Загружаем изображение телефона
    if not os.path.exists(phone_image_path):
        print(f"Файл изображения {phone_image_path} не найден!")
        return
    phone_image = Image.open(phone_image_path)

    # Вычисляем координаты для размещения телефона по центру
    phone_x = (width - phone_image.width) // 2
    phone_y = (height - phone_image.height) // 2

    # Накладываем изображение телефона на фон
    bg.paste(phone_image, (phone_x, phone_y), phone_image if phone_image.mode == 'RGBA' else None)

    # Сохраняем результат
    bg.save(output_path, "PNG")
    print(f"Страница с изображением телефона сохранена как {output_path}")

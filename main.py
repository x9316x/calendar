import os

from create_title_image import create_title_image
from create_month_images import create_month_images_with_background

def main():
    # Каталоги для шрифтов и изображений
    fonts_dir = "fonts"
    images_dir = "images"

    # Пути к файлам
    font_path = os.path.join(fonts_dir, "ofont.ru_Uncage.ttf")
    background_image = os.path.join(images_dir, "background.png")
    output_folder = "months_png"

    # Проверка существования каталогов
    if not os.path.exists(fonts_dir):
        print(f"Каталог с шрифтами не найден: {fonts_dir}")
        return

    if not os.path.exists(images_dir):
        print(f"Каталог с изображениями не найден: {images_dir}")
        return

    # Генерация слайдов
    print("Генерация титульного слайда...")
    create_title_image(output_folder, background_image, font_path)

    print("Генерация календарных изображений...")
    create_month_images_with_background(output_folder, background_image, font_path)

if __name__ == "__main__":
    main()

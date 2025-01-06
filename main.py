import os

from create_month_images import create_month_images_with_background

def main():
    # Каталоги для шрифтов и изображений
    fonts_dir = "fonts"
    images_dir = "images"

    # Пути к файлам
    font_path = os.path.join(fonts_dir, "ofont.ru_Uncage.ttf")
    font_arial_path = os.path.join(fonts_dir, "ofont.ru_Arial.ttf")
    background_image = os.path.join(images_dir, "background.png")
    output_folder = "months_png"
    phone_image = os.path.join(images_dir, "phone.png")
    # phone_image_2 = os.path.join(images_dir, "phone_2.png")
    phone_image_1 = os.path.join(images_dir, "phone_2_1.png")
 

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
    create_month_images_with_background(output_folder, background_image, font_path, text_color)



if __name__ == "__main__":
    main()

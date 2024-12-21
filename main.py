import os

from create_title_image import create_title_image
from create_month_images import create_month_images_with_background

from create_ganeral_image_1 import create_ganeral_image_1
from create_ganeral_image_2 import create_ganeral_image_2
from create_ganeral_image_3 import create_ganeral_image_3
from create_ganeral_image_4 import create_ganeral_image_4
from create_ganeral_image_5 import create_ganeral_image_5
from create_ganeral_image_6 import create_ganeral_image_6
from create_ganeral_image_7 import create_ganeral_image_7
from create_ganeral_image_8 import create_ganeral_image_8

def main():
    # Каталоги для шрифтов и изображений
    fonts_dir = "fonts"
    images_dir = "images"

    # Пути к файлам
    font_path = os.path.join(fonts_dir, "ofont.ru_Uncage.ttf")
    background_image = os.path.join(images_dir, "background.png")
    output_folder = "months_png"
    phone_image = os.path.join(images_dir, "phone.png")
    phone_image_2 = os.path.join(images_dir, "phone_2.png")

    # Проверка существования каталогов
    if not os.path.exists(fonts_dir):
        print(f"Каталог с шрифтами не найден: {fonts_dir}")
        return

    if not os.path.exists(images_dir):
        print(f"Каталог с изображениями не найден: {images_dir}")
        return

    # Генерация слайдов
    # print("Генерация титульного слайда...")
    create_title_image(output_folder, background_image, font_path)

    # print("Генерация общего слайда 1...")
    create_ganeral_image_1(output_folder, background_image, font_path)

    # print("Генерация общего слайда 2...")
    create_ganeral_image_2(output_folder, background_image, font_path)
    
    # print("Генерация общего слайда 3...")
    create_ganeral_image_3(output_folder, background_image, phone_image)

    
    # print("Генерация общего слайда 4...")
    create_ganeral_image_4(output_folder, background_image, font_path)

    # print("Генерация общего слайда 5...")
    create_ganeral_image_5(output_folder, background_image, font_path)

    # print("Генерация общего слайда 6...")
    create_ganeral_image_6(output_folder, background_image, phone_image_2)
    
    # print("Генерация общего слайда 7...")
    create_ganeral_image_7(output_folder, background_image, font_path)


    # print("Генерация общего слайда 8...")
    create_ganeral_image_8(output_folder, background_image, font_path)

    # # print("Генерация календарных изображений...")
    create_month_images_with_background(output_folder, background_image, font_path)

if __name__ == "__main__":
    main()

import os

from create_month_images_1 import create_month_images_with_background_1
from create_month_images_2 import create_month_images_with_background_2
from create_month_images_3 import create_month_images_with_background_3
from create_month_images_4 import create_month_images_with_background_4
from create_month_images_5 import create_month_images_with_background_5
from create_month_images_6 import create_month_images_with_background_6
from create_month_images_7 import create_month_images_with_background_7
from create_month_images_8 import create_month_images_with_background_8
from create_month_images_9 import create_month_images_with_background_9


def main():
    # Каталоги для шрифтов и изображений
    fonts_dir = "fonts"
    images_dir = "images"

    # Пути к файлам
    font_path = os.path.join(fonts_dir, "ofont.ru_Uncage.ttf")
    background_image = os.path.join(images_dir, "background.png")
    
    # output_folder_1 = "months_png/1"
    # output_folder_2 = "months_png/2"
    # output_folder_3 = "months_png/3"
    # output_folder_4 = "months_png/4"
    # output_folder_5 = "months_png/5"
    # output_folder_6 = "months_png/6"
    # output_folder_7 = "months_png/7"
    # output_folder_8 = "months_png/8"
    # output_folder_9 = "months_png/9"
 
    output_folder_1 = "all_years/1"
    output_folder_2 = "all_years/2"
    output_folder_3 = "all_years/3"
    output_folder_4 = "all_years/4"
    output_folder_5 = "all_years/5"
    output_folder_6 = "all_years/6"
    output_folder_7 = "all_years/7"
    output_folder_8 = "all_years/8"
    output_folder_9 = "all_years/9"

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
    create_month_images_with_background_1(output_folder_1, background_image, font_path, text_color)
    create_month_images_with_background_2(output_folder_2, background_image, font_path, text_color)
    create_month_images_with_background_3(output_folder_3, background_image, font_path, text_color)
    create_month_images_with_background_4(output_folder_4, background_image, font_path, text_color)
    create_month_images_with_background_5(output_folder_5, background_image, font_path, text_color)
    create_month_images_with_background_6(output_folder_6, background_image, font_path, text_color)
    create_month_images_with_background_7(output_folder_7, background_image, font_path, text_color)
    create_month_images_with_background_8(output_folder_8, background_image, font_path, text_color)
    create_month_images_with_background_9(output_folder_9, background_image, font_path, text_color)



if __name__ == "__main__":
    main()

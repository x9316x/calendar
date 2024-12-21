from PIL import Image
import os
import glob

def stitch_images_to_pdf(input_folder="months_png", output_pdf="calendar_2025.pdf"):
    """Создание PDF из PNG-изображений."""
    if os.path.exists(output_pdf):
        os.remove(output_pdf)

    # Добавляем титульный слайд
    title_image_path = "title.png"
    if not os.path.exists(title_image_path):
        print(f"Ошибка: Файл титульного слайда {title_image_path} не найден!")
        return

    image_paths = [title_image_path]  # Начинаем с титульного изображения
    # Добавляем остальные изображения
    month_images = sorted(glob.glob(os.path.join(input_folder, "*.png")))
    if not month_images:
        print("Ошибка: Не найдены файлы PNG для сборки PDF.")
        return
    image_paths.extend(month_images)  # Объединяем пути

    # Открываем изображения
    images = [Image.open(image_path) for image_path in image_paths]

    # Сшиваем изображения в PDF
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"Календарь сохранён как {output_pdf}")


if __name__ == "__main__":
    input_folder = "months_png"
    output_pdf = "calendar_2025.pdf"

    print("Создание PDF из PNG...")
    stitch_images_to_pdf(input_folder, output_pdf)

from PIL import Image
import os
import glob

def stitch_images_to_pdf(input_folder="months_png", title_image="months_png/00_Титульный.png", output_pdf="calendar_2025.pdf"):
    """Создание PDF из PNG-изображений."""
    # Удаляем существующий PDF, если есть
    if os.path.exists(output_pdf):
        os.remove(output_pdf)

    # Проверяем наличие титульного слайда
    if not os.path.exists(title_image):
        print(f"Ошибка: Титульное изображение {title_image} не найдено!")
        return

    # Собираем изображения
    image_paths = [title_image]  # Добавляем титульный слайд
    month_images = sorted(glob.glob(os.path.join(input_folder, "*.png")))
    if not month_images:
        print("Ошибка: Не найдены файлы PNG для сборки PDF.")
        return
    image_paths.extend(month_images)  # Добавляем остальные изображения

    # Открываем изображения
    images = [Image.open(image_path) for image_path in image_paths]

    # Создаём PDF
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"Календарь сохранён как {output_pdf}")

if __name__ == "__main__":
    # Параметры для запуска
    input_folder = "months_png"
    title_image = os.path.join(input_folder, "00_Титульный.png")
    output_pdf = "calendar_2025.pdf"

    print("Создание PDF из PNG...")
    stitch_images_to_pdf(input_folder, title_image, output_pdf)
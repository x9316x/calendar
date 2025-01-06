from PIL import Image
import os
import glob

def stitch_images_to_pdf(input_folder, title_image, output_pdf):
    """Создание PDF из PNG-изображений."""
    if os.path.exists(output_pdf):
        os.remove(output_pdf)

    # Проверяем наличие титульного слайда
    if not os.path.exists(title_image):
        print(f"Ошибка: Титульное изображение {title_image} не найдено!")
        return

    # Собираем пути к изображениям
    image_paths = [title_image]  # Добавляем титульный слайд
    month_images = sorted(glob.glob(os.path.join(input_folder, "*.png")))

    # Исключаем титульный файл, если он уже в папке
    month_images = [img for img in month_images if os.path.basename(img) != os.path.basename(title_image)]

    # Добавляем остальные изображения
    image_paths.extend(month_images)

    # Открываем изображения
    images = [Image.open(image_path) for image_path in image_paths]

    # Сшиваем изображения в PDF
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"Календарь сохранён как {output_pdf}")

def process_all_folders(base_folder="all_years", output_prefix="calendar"):
    """Создание PDF для каждой папки внутри базовой папки."""
    if not os.path.exists(base_folder):
        print(f"Ошибка: Папка {base_folder} не найдена!")
        return

    # Находим все подкаталоги в базовой папке
    subfolders = sorted([f.path for f in os.scandir(base_folder) if f.is_dir()])

    for idx, folder in enumerate(subfolders, start=1):
        print(f"Обработка папки: {folder}")

        # Генерируем пути
        title_image = os.path.join(folder, "00_Титульный.png")
        output_pdf = f"{output_prefix}_{idx}.pdf"

        # Проверяем, что титульный файл существует
        if not os.path.exists(title_image):
            print(f"Ошибка: Титульный файл {title_image} не найден в {folder}!")
            continue

        # Создаём PDF для текущей папки
        stitch_images_to_pdf(folder, title_image, output_pdf)

if __name__ == "__main__":
    # Параметры для запуска
    base_folder = "all_years"  # Папка, содержащая 9 папок с изображениями
    output_prefix = "calendar"  # Префикс для названий выходных файлов

    print("Создание PDF для всех папок...")
    process_all_folders(base_folder, output_prefix)

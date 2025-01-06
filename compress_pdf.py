import fitz  # PyMuPDF
from PIL import Image
import io
import os

def compress_pdf(input_path, output_path, image_quality=50):
    """
    Сжимает PDF, уменьшая качество изображений.
    :param input_path: Путь к исходному PDF-файлу.
    :param output_path: Путь к сжатому PDF-файлу.
    :param image_quality: Качество изображений (1-100), где 100 — максимальное.
    """
    try:
        # Открываем PDF
        pdf_document = fitz.open(input_path)
        new_pdf = fitz.open()

        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            pix = page.get_pixmap()

            # Конвертируем Pixmap в изображение
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

            # Сохраняем изображение в JPEG с нужным качеством
            img_buffer = io.BytesIO()
            img.save(img_buffer, format="JPEG", quality=image_quality)
            img_buffer.seek(0)

            # Создаём новую страницу и вставляем сжатое изображение
            new_page = new_pdf.new_page(width=pix.width, height=pix.height)
            new_page.insert_image(new_page.rect, stream=img_buffer.getvalue())

        # Сохраняем сжатый PDF
        new_pdf.save(output_path)
        print(f"PDF успешно сжат и сохранён в {output_path}")
    except Exception as e:
        print(f"Ошибка: {e}")

# Список входных и выходных файлов
input_folder = "input_pdfs"  # Папка с исходными PDF
output_folder = "compressed_pdfs"  # Папка для сжатых PDF
os.makedirs(output_folder, exist_ok=True)

# Обработка всех PDF в папке
for i in range(1, 10):  # Обрабатываем файлы calendar_1.pdf ... calendar_9.pdf
    input_pdf = os.path.join(input_folder, f"calendar_{i}.pdf")
    output_pdf = os.path.join(output_folder, f"year_{i}.pdf")
    compress_pdf(input_pdf, output_pdf, image_quality=50)  # Качество 50%

# ImageProcessor — класс для обработки изображения (применение фильтров, добавление текста, поворот).
from PIL import ImageFilter, ImageDraw, ImageFont # импортируем необходимые классы для обработки изображений

class ImageProcessor:
    def __init__(self, image):
        if image is None: # проверяем, передано ли изображение
            raise ValueError("Изображение не может быть None.")
        self.image = image # сохраняем изображение для дальнейшей обработки

    def apply_filter(self, filter_type='BLUR'):
        if self.image is None:
            raise ValueError("Изображение не загружено.")
        try:
            if filter_type == 'BLUR':
                self.image = self.image.filter(ImageFilter.BLUR) # применяем фильтр размытия
                print("Применен фильтр размытия.")
            else:
                raise ValueError("Неизвестный тип фильтра.") # если фильтр не распознан, выбрасываем исключение
        except Exception as e:
            raise Exception(f"Ошибка при применении фильтра: {e}")

    def add_text(self, text, position=None, font_size=20):
        if self.image is None:
            raise ValueError("Изображение не загружено.")
        try:
            draw = ImageDraw.Draw(self.image) # создаем объект для рисования на изображении
            font = ImageFont.load_default() # загружаем шрифт по умолчанию

            text_bbox = draw.textbbox((0, 0), text, font=font) # получаем границы текста
            text_width = text_bbox[2] - text_bbox[0] # вычисляем ширину текста
            text_height = text_bbox[3] - text_bbox[1] # вычисляем высоту текста

            if position is None: # если позиция не указана
                position = (self.image.width - text_width - 20, self.image.height - text_height - 20)

            draw.text(position, text, fill="white", font=font) # добавляем текст на изображение
            print("Текст добавлен на изображение.")
        except Exception as e:
            raise Exception(f"Ошибка при добавлении текста: {e}")

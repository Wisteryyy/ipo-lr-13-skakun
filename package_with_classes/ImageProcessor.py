# ImageProcessor — класс для обработки изображения (применение фильтров, добавление текста, поворот).
from PIL import ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_filter(self, filter_type='BLUR'):
        if self.image:
            if filter_type == 'BLUR':
                self.image = self.image.filter(ImageFilter.BLUR)
                print("Применен фильтр размытия.")
            elif filter_type == 'CONTOUR':
                self.image = self.image.filter(ImageFilter.CONTOUR)
                print("Применен контурный фильтр.")
        else:
            print("Изображение не загружено.")

    def add_text(self, text, position=None, font_size=20):
        if self.image:
            draw = ImageDraw.Draw(self.image)
            font = ImageFont.load_default()
            
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            if position is None:
                position = (self.image.width - text_width - 10, self.image.height - text_height - 10)

            draw.text(position, text, fill="white", font=font)
            print("Текст добавлен на изображение.")
        else:
            print("Изображение не загружено.")

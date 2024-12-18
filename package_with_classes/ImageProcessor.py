from PIL import ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_filter(self, filter_type='BLUR'):
        if self.image:
            if filter_type == 'BLUR':
                self.image = self.image.filter(ImageFilter.BLUR)
                print("Применен фильтр размытия.")
        else:
            print("Изображение не загружено.")

    def add_text(self, text, position=(10, 10), font_size=20):
        if self.image:
            draw = ImageDraw.Draw(self.image)
            font = ImageFont.load_default()
            draw.text(position, text, fill="white", font=font)
            print("Текст добавлен на изображение.")
        else:
            print("Изображение не загружено.")

    def rotate_image(self, angle):
        if self.image:
            self.image = self.image.rotate(angle)
            print(f"Изображение повернуто на {angle} градусов.")
        else:
            print("Изображение не загружено.")
from PIL import Image
from .ImageProcessor import ImageProcessor

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.filename = None

    def load_image(self):
        try:
            self.image = Image.open(self.image_path)
            self.filename = self.image_path.split("\\")[-1]
            print(f'Изображение загружено: {self.image_path}')
        except Exception as e:              
            print(f"Произошла ошибка при загрузке изображения: {e}")

    def save_image(self, save_path):
        if self.image:
            self.image.save(save_path, format='PNG')
            print(f'Изображение сохранено как: {save_path}')
        else:
            print("Изображение не загружено.")

    def resize_image(self, new_size=(200, 200)):
        if self.image:
            self.image = self.image.resize(new_size)
            print(f'Изображение изменено до: {new_size}')
        else:
            print("Изображение не загружено.")

    def get_processor(self):
        return ImageProcessor(self.image)
# ImageHandler — класс для базовой работы с изображениями (загрузка, сохранение, изменение размеров и форматов).
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
        except FileNotFoundError:
            print(f"Файл не найден: {self.image_path}. Проверьте путь к изображению.")
        except Exception as e:
            print(f"Произошла ошибка при загрузке изображения: {e}")

    def save_image(self, save_path):
        if self.image:
            try:
                self.image.save(save_path, format='PNG')
                print(f'Изображение сохранено как: {save_path}')
            except Exception as e:
                print(f"Произошла ошибка при сохранении изображения: {e}")
        else:
            print("Изображение не загружено. Сначала загрузите изображение.")

    def resize_image(self, new_size=(300, 300)):
        if self.image:
            try:
                self.image = self.image.resize(new_size)
                print(f'Изображение изменено до: {new_size}')
            except Exception as e:
                print(f"Произошла ошибка при изменении размера изображения: {e}")
        else:
            print("Изображение не загружено. Сначала загрузите изображение.")

    def get_processor(self):
        if self.image:
            return ImageProcessor(self.image)
        else:
            print("Изображение не загружено. Сначала загрузите изображение.")
            return None

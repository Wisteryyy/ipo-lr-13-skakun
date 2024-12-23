# ImageHandler — класс для базовой работы с изображениями (загрузка, сохранение, изменение размеров и форматов).
from PIL import Image # импортируем класс Image из библиотеки PIL для работы с изображениями

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path # сохраняем путь к изображению
        self.image = None # инициализируем переменную для хранения изображения
        self.filename = None # инициализируем переменную для хранения имени файла

    def load_image(self):
        try:
            self.image = Image.open(self.image_path) # загружаем изображение по указанному пути
            self.filename = self.image_path.split("/")[-1] # извлекаем имя файла из пути
            print(f'Изображение загружено: {self.filename}')
        except FileNotFoundError:
            raise FileNotFoundError("Файл не найден. Проверьте путь к изображению.")
        except Exception as e:
            raise Exception(f"Ошибка при загрузке изображения: {e}")

    def save_image(self, save_path):
        if self.image is None: # проверяем, загружено ли изображение
            raise ValueError("Изображение не загружено. Сначала загрузите изображение.")
        try:
            self.image.save(save_path, format='PNG') # сохраняем изображение по указанному пути в формате PNG
            print(f'Изображение сохранено как: {save_path}')
        except Exception as e:
            raise Exception(f"Ошибка при сохранении изображения: {e}")

    def resize_image(self, new_size=(300, 300)):
        if self.image is None:
            raise ValueError("Изображение не загружено. Сначала загрузите изображение.")
        try:
            self.image = self.image.resize(new_size) # изменяем размер изображения на указанный
            print(f'Изображение изменено до: {new_size}')
        except Exception as e:
            raise Exception(f"Ошибка при изменении размера изображения: {e}")

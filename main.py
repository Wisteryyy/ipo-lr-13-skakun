from package_with_classes.ImageHandler import ImageHandler
from package_with_classes.ImageProcessor import ImageProcessor

images = []
Status = True

def print_menu():
    print("------------------------------------------------------------------------------")
    print("--------------------------- Выберите пункт меню-------------------------------") 
    print("-----1. Загрузить изображение.------------------------------------------------") 
    print("-----2. Сохранить изображение.------------------------------------------------") 
    print("-----3. Использовать Thumbnail (200x200) для изображения.---------------------") 
    print("-----4. Использовать ImageProcessor (контур) для изображения.-----------------") 
    print("-----5. Использовать ImageProcessor (добавить текст в центр) для изображения.-") 
    print("-----6. Список изображений в памяти программы.--------------------------------") 
    print("-----7. Просмотреть изображение из памяти программы.--------------------------") 
    print("-----8. Завершить выполнение программы.----------------------------------------") 
    print("------------------------------------------------------------------------------")

def print_images(): 
    print("------------------------------------------------------------------------------")
    counter = 0 
    for image in images: 
        counter += 1 
        print(f"{counter}. {image.filename}") 
    print() 

while Status: 
    print_menu() 
    input_data = input("Введите нужное значение: ") 
    try: 
        input_data = int(input_data) 
    except ValueError: 
        print("Введите корректное значение!") 
        continue

    if input_data == 1: 
        print("------------------------------------------------------------------------------")
        input_data = input("Укажите путь до изображения, которое хотите загрузить в память: ") 
        try: 
            images.append(ImageHandler(input_data)) 
            images[-1].load_image()
            print("Изображение успешно добавлено!") 
        except FileNotFoundError: 
            print("Файл не найден. Проверьте корректность введенных данных") 

    elif input_data == 2: 
        print_images() 
        input_data = input("Выберите изображение, которое хотите сохранить: ") 
        try: 
            input_data = int(input_data) 
            name = input("Введите название сохраняемого изображения: ") 
            images[input_data - 1].save_image(name) 
            print("Успешно сохранено!")
        except (IndexError, ValueError): 
            print("Не удалось найти изображение. Проверьте корректность введенных данных!") 

    elif input_data == 3: 
        print_images() 
        input_data = input("Выберите изображение, на котором хотите использовать Thumbnail (200x200): ") 
        try: 
            input_data = int(input_data) 
            images[input_data - 1].resize_image((200, 200))
            print("Thumbnail (200x200) для изображения успешно применен!") 
        except (IndexError, ValueError): 
            print("Файл не найден. Проверьте корректность введенных данных") 

    elif input_data == 4: 
        print_images() 
        input_data = input("Выберите изображение, на котором хотите использовать ImageProcessor (контур): ") 
        try: 
            input_data = int(input_data) 
            processor = ImageProcessor(images[input_data - 1].image)
            processor.apply_filter('CONTOUR')
            print("ImageProcessor (контур) для изображения успешно применен!") 
        except (IndexError, ValueError): 
            print("Файл не найден. Проверьте корректность введенных данных") 

    elif input_data == 5: 
        print_images() 
        input_data = input("Выберите изображение, на котором хотите использовать ImageProcessor (добавить текст в центр): ") 
        try: 
            input_data = int(input_data) 
            text = input("Введите текст для добавления: ")
            processor = ImageProcessor(images[input_data - 1].image)
            processor.add_text(text)
            print("ImageProcessor (добавить текст в центр) для изображения успешно применен!") 
        except (IndexError, ValueError): 
            print("Файл не найден. Проверьте корректность введенных данных") 

    elif input_data == 6: 
        print("Вот список изображений в памяти программы: ") 
        print_images() 

    elif input_data == 7: 
        print_images() 
        input_data = input("Выберите изображение, которое хотите просмотреть: ") 
        try: 
            input_data = int(input_data) 
            images[input_data - 1].image.show()
        except (IndexError, ValueError): 
            print("Файл не найден. Проверьте корректность введенных данных") 

    elif input_data == 8: 
        print("Завершение выполнения программы.") 
        Status = False

    else:
        print("Неверный выбор. Попробуйте снова.")
import os
import shutil

while True:
    def create_file(file_name):
        try:
            with open(file_name, 'w'):
                pass
            print(f"Файл {file_name} успешно создан.")
        except IOError:
            print(f"Не удалось создать файл {file_name}.")

    def delete_file(file_name):
        try:
            os.remove(file_name)
            print(f"Файл {file_name} успешно удален.")
        except FileNotFoundError:
            print(f"Файл {file_name} не найден.")

    def create_folder(folder_name):
        try:
            os.mkdir(folder_name)
            print(f"Папка {folder_name} успешно создана.")
        except FileExistsError:
            print(f"Папка {folder_name} уже существует.")

    def delete_folder(folder_name):
        try:
            os.rmdir(folder_name)
            print(f"Папка {folder_name} успешно удалена.")
        except FileNotFoundError:
            print(f"Папка {folder_name} не найдена.")

    def move(src, dest):
        try:
            os.replace(src, dest)
            print(f"Успешно перемещено {src} в {dest}.")
        except FileNotFoundError:
            print(f"Файл или папка не найдены.")

    def copy_file(src, dest):
        try:
            shutil.copy2(src, dest)
            print(f"Файл {src} успешно скопирован в {dest}.")
        except FileNotFoundError:
            print(f"Файл {src} не найден.")
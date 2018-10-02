import os


def print_list(list_dir):
    for item in list_dir:
        print(item)


def main():
    global list_dir
    end = False

    while not end:

        track = input("Для выхода введите exit\nДля выбора данной директории введите enter\nВведите директорию: ")

        if os.path.isdir(track):
            os.chdir(track)
            print("Вы находитесь в директории: ", os.getcwd())
            list_dir = os.listdir(".")
            print_list(list_dir)
        elif track == "exit":
            end = True
        elif track == "enter":
            # sangaklgagaglaalg
            end = True
        else:
            print("Неверный ввод!!!")
            print("Вы находитесь в директории: ", os.getcwd())

#Вызов основной функции
main()

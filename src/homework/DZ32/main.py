from work_to_dict import WorkToDict as WTDict
from countries import Countries
from music_group import MusicGroup as MusGr

def work_to_dict_menu(obj: WTDict, theme : str = ""):
    choice = ""

    while choice != "0":
        print(f"\n{theme}")
        print(f"1. Добавить информацию.\n"
              f"2. Удалить информацию.\n"
              f"3. Поиск информации.\n"
              f"4. Редактировать информацию.\n"
              f"5. Сохранить информацию.\n"
              f"6. Загрузить информацию.\n"
              f"7. Показать информацию\n"
              f"0. Назад в меню")

        choice = input("Введите нужную команду: ")

        match choice:

            case "1":
                obj.add_info()
            case "2":
                obj.del_info()
            case "3":
                obj.search_info()
            case "4":
                obj.edit_info()
            case "5":
                obj.save_info()
            case "6":
                obj.load_info()
            case "7":
                print(obj)
            case "0":
                pass
            case _:
                print(f"Нет такой команды - {choice}")


def main():
    choice = ""

    while choice != "0":
        print("\n1. Страны\n"
              "2. Музыкальные группы\n"
              "0. Выход из программы")

        choice = input("Выберете пункт: ")

        match choice:

            case "1":
                countries = Countries()
                work_to_dict_menu(countries, "СТРАНЫ")
            case "2":
                mus_gr = MusGr()
                work_to_dict_menu(mus_gr, "МУЗЫКАЛЬНЫЕ ГРУППЫ")
            case "0":
                print("До свидания")
            case _:
                print(f"Нет такой команды - {choice}")

main()
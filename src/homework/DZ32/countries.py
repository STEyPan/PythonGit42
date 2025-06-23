from work_to_dict import WorkToDict as WTD

class Countries(WTD):
    def __init__(self, dictionary: dict = {}):
        super().__init__(dictionary)

    def __del__(self):
        pass

    def __str__(self):
        return (f"\nСтрана - Столица\n"
                f"{super().__str__()}")

    def add_info(self):
        key = input("Введите название страны: ")

        if key not in self._dictionary:
            value = input("Введите название столицы: ")
            self.add_info_logic(key, value)
        else:
            print(f"Страна {key} уже есть в словаре")

    def del_info(self):
        key = input("Введите название страны, информацию о которой ВЫ хотите удалить: ")

        if key in self._dictionary:
            self.del_info_logic(key)
            print(f"Информация о стране {key} удалена")
        else:
            print(f"Страна {key} не найдена")

    def search_info(self):
        key = input("Введите название страны, информацию о которой ВЫ хотите найти: ")

        if key in self._dictionary:
            print(f"Столица страны {key} - {self.search_info_logic(key)}")
        else:
            print(f"Страна {key} не найдена")

    def edit_info(self):
        key = input("Введите название страны, информацию о которой ВЫ хотите изменить: ")

        if key in self._dictionary:
            new_value = input("Введите название новой столицы: ")
            self.edit_info_logic(key, new_value)
        else:
            print(f"Страна {key} не найдена")

    def save_info(self):
        name_file = "countries"
        self.save_info_logic(name_file)
        print("\nДанные сохранены\n")

    def load_info(self):
        name_file = "countries"
        self.load_info_logic(name_file)
        print("\nДанные загружены\n")
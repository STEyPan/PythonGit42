from work_to_dict import WorkToDict as WTD

class MusicGroup(WTD):
    def __init__(self, dictionary: dict = {}):
        super().__init__(dictionary)

    def __del__(self):
        pass

    def __str__(self):
        title = "\nМузыкальная группа - Альбомы"
        table = "\n".join([f"{key} - {", ".join(values)}" for key, values in self._dictionary.items()])
        return f"{title}\n{table}"

    def add_info(self):
        key = input("Введите название группы: ")

        if key in self._dictionary:
            print(f"Музыкальная группа {key} уже есть в словаре")
        else:
            value = []

            count_albums = int(input("Сколько альбомов ВЫ хотите добавить?  "))

            while count_albums != 0:
                album = input("Введите название альбома: ")
                count_albums -= 1
                value.append(f"«{album}»")

            self.add_info_logic(key, value)


    def del_info(self):
        key = input("Введите название муз.группы, информацию о которой ВЫ хотите удалить: ")

        if key in self._dictionary:
            self.del_info_logic(key)
        else:
            print(f"Музыкальная группа {key} не найдена")

    def search_info(self):
        key = input("Введите название муз.группы, информацию о которой ВЫ хотите найти: ")

        if key in self._dictionary:
            albums = self.search_info_logic(key)
            print(f"Альбомы группы {key} - {", ".join(albums)}")
        else:
            print(f"Музыкальная группа {key} не найдена")

    def edit_info(self):
        key = input("Введите название муз.группы, информацию о которой ВЫ хотите изменить: ")

        if key not in self._dictionary:
            print(f"Музыкальная группа {key} не найдена")
        else:
            new_value = []

            count_albums = int(input("Сколько альбомов ВЫ хотите добавить?  "))

            while count_albums != 0:
                album = input("Введите название альбома: ")
                count_albums -= 1
                new_value.append(f"«{album}»")

            self.edit_info_logic(key, new_value)

    def save_info(self):
        name_file = "music_group"
        self.save_info_logic(name_file)
        print("\nДанные сохранены\n")

    def load_info(self):
        name_file = "music_group"
        self.load_info_logic(name_file)
        print("\nДанные загружены\n")
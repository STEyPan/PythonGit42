import json

class WorkToDict:
    _dictionary = dict()

    def __init__(self, dictionary : dict = {}):
        self._dictionary = dictionary

    def __del__(self):
        pass

    def __str__(self):
        fulltext = f"{"\n".join([f"{key} - {value}" 
                             for key, value in self._dictionary.items()])}\n"
        return fulltext if self._dictionary else "Словарь пуст"

    def add_info_logic(self, key, value):
        if key not in self._dictionary:
            self._dictionary[key] = value

    def add_info(self):
        pass

    def del_info_logic(self, key):
        if key in self._dictionary:
            del self._dictionary[key]

    def del_info(self):
        pass

    def search_info_logic(self, key):
        if key in self._dictionary:
            return self._dictionary[key]

    def search_info(self):
        pass

    def edit_info_logic(self, key, new_value):
        if key in self._dictionary:
            self._dictionary[key] = new_value

    def edit_info(self):
        pass

    def save_info_logic(self, name_file):
        with open(f"{name_file}.json", "w", encoding="utf-8") as file:
            json.dump(self._dictionary, file, ensure_ascii=False)

    def save_info(self):
        pass

    def load_info_logic(self, name_file):
        with open(f"{name_file}.json", "r", encoding="utf-8") as file:
            self._dictionary = json.load(file)

    def load_info(self):
        pass
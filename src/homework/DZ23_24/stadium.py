class Stadium:
    __name = str()
    __date = 1970
    __country = str()
    __city = str()
    __capacity = 0

    def __init__(self,
                 name: str = "Название",
                 date: int = 1970,
                 country: str = "Страна",
                 city: str = "Город",
                 capacity: str = "Вместимость"):

        self.__name = name
        self.__date = date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def __del__(self):
        pass

    def input_data(self,
                   name: str = None,
                   date: int = None,
                   country: str = None,
                   city: str = None,
                   capacity: str = None
                   ):

        self.__name = name if name != None else self.__name
        self.__date = date if date != None else self.__date
        self.__country = country if country != None else self.__country
        self.__city = city if city != None else self.__city
        self.__capacity = capacity if capacity != None else self.__capacity


    def get_data(self):
        return (f"Название стадиона: {self.__name}\n"
                f"Дата открытия: {self.__date}\n"
                f"Страна: {self.__country}\n"
                f"Город: {self.__city}\n"
                f"Вместимость: {self.__capacity}")

    @property
    def stadium_name(self):
        return self.__name

    @stadium_name.setter
    def stadium_name(self, new_name: str = None):
        if new_name != None:
            self.__name = new_name

    @property
    def stadium_date(self):
        return self.__name

    @stadium_date.setter
    def stadium_date(self, new_date: int = None):
        if new_date != None:
            self.__date = new_date

    @property
    def stadium_country(self):
        return self.__name

    @stadium_country.setter
    def stadium_country(self, new_country: str = None):
        if new_country != None:
            self.__country = new_country

    @property
    def stadium_city(self):
        return self.__name

    @stadium_city.setter
    def stadium_city(self, new_city: str = None):
        if new_city != None:
            self.__city = new_city

    @property
    def stadium_capacity(self):
        return self.__name

    @stadium_capacity.setter
    def stadium_capacity(self, new_capacity: int = None):
        if new_capacity != None:
            self.__capacity = new_capacity
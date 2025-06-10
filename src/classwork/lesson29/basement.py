from home import Home

class Basement(Home):

    __type_basement = str()
    __communications = list()

    def __init__(self,
                 area : float = 0.0,
                 input_power : float = 0.0,
                 type_basement : str = "",
                 communications : list = []):

        super().__init__(area, input_power)
        self.__type_basement = type_basement
        self.__communications = communications

    def __del__(self):
        super().__del__()

    def total_cost(self):

        basement_prices = {
            "свайный" : 20,
            "плитный" : 30,
            "ленточный" : 40,
            "столбчатый" : 50
        }

        communications_prices = {
            "вода" : 2000,
            "газ" : 3000,
            "электричество" : 4000
        }

        sum_input_power = self._input_power * 5
        basement_price = 0
        communications_price = 0


        for key, value in basement_prices.items():
            if self.__type_basement.lower() == key:
                basement_price = value * self._area


        for key, value in communications_prices.items():
            for elem in self.__communications:
                if elem.lower() == key:
                    communications_price += value


        return sum_input_power + basement_price + communications_price



basement_1 = Basement(area=200, type_basement="свайный",input_power=2000, communications=["Вода", "Газ"])
print(basement_1.total_cost())
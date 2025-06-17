class AdditionalOptions:
    __options = list()

    def __init__(self, options : list = list):

        self.__options = options

    def __del__(self):
        pass

    def total_cost(self):
        return len(self.__options) * 2000

    def __str__(self):
        return (f"\n------ Дополнительные опции ------\n"
                f"\t-{"\n\t-".join(self.__options)}\n"
                f"Общая стоимость: {self.total_cost():,} рублей")



# add_opt = AdditionalOptions(["a","b","c","d"])
# print(add_opt)
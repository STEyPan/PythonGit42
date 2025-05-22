class Roman:
    __arab_digit = 0
    __rome_digit = ""

    __rome_to_arab = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100
        }

    def __init__(self, digit: str = "", int_digit: int = 0):

        if digit:
            self.__rome_digit = digit

        elif int_digit:
            self.__arab_digit = int_digit

    def __del__(self):
        pass

    def __romeToInt(self, digit):

        rome_to_arab = self.__rome_to_arab

        lvl = 0
        temp = 0
        result = 0

        for char in digit[::-1]:

            if rome_to_arab[char] >= lvl:
                result += temp
                lvl = rome_to_arab[char]
                temp = rome_to_arab[char]

            else:
                temp -= rome_to_arab[char]

        result += temp

        return result


    def __intToRome(self, int_digit: int) -> str:
        # roman = ""
        # alpha_lst = ["C", "L", "X", "V", "I"]
        #
        # for key in alpha_lst:
        #
        #     while int_digit - self.__rome_to_arab[key] >= 0:
        #         int_digit -= self.__rome_to_arab[key]
        #         roman += key
        # # 4
        # if "IIII" in roman:
        #     roman = roman.replace("IIII","IV")
        # # 9
        # if "VIV" in roman:
        #     roman = roman.replace("VIV", "IX")
        # # 40
        # if "XXXX" in roman:
        #     roman = roman.replace("XXXX", "XL")
        # # 49
        # if "XLIX" in roman:
        #     pass

        arab_to_rome = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        result = ""

        for arab, rome in arab_to_rome:
            while int_digit >= arab:
                result += rome
                int_digit -= arab

        return result


    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(self.__arab_digit + other.__arab_digit)
        elif isinstance(other, int):
            return Roman(self.__arab_digit + other)
        else:
            raise "Ошибка типов"

    def __sub__(self, other):
        if isinstance(other, Roman):
            return Roman(self.__arab_digit - other.__arab_digit)
        elif isinstance(other, int):
            return Roman(self.__arab_digit - other)
        else:
            raise "Ошибка типов"

    def __mul__(self, other):
        if isinstance(other, Roman):
            return Roman(self.__arab_digit * other.__arab_digit)
        elif isinstance(other, int):
            return Roman(self.__arab_digit * other)
        else:
            raise "Ошибка типов"

    def __truediv__(self, other):
        if isinstance(other, Roman):
            return Roman(self.__arab_digit / other.__arab_digit)
        elif isinstance(other, int):
            return Roman(self.__arab_digit / other)
        else:
            raise "Ошибка типов"

    def __str__(self):
        return f"{self.__rome_digit}"
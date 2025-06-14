from money import Money

class Rub(Money):

    def __init__(self, whole: int = 0, cent: int = 0):
        super().__init__(whole, cent)

    def __del__(self):
        super().__del__()

    def __str__(self):
        return f"{self._whole} рублей{f" {self._cent} копеек" if self._cent > 0 else ""}"

    def __add__(self, other):
        if isinstance(other, Rub):

            sum_whole = self._whole + other._whole
            sum_cent = self._cent + other._cent

            if sum_cent > 99:
                sum_whole += 1
                sum_cent %= 100

            return Rub(sum_whole, sum_cent)
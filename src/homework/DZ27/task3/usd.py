from money import Money

class USD(Money):
    def __init__(self, whole: int = 0, cent: int = 0):
        super().__init__(whole, cent)

    def __del__(self):
        super().__del__()

    def __str__(self):
        return f"{self._whole} долларов{f" {self._cent} центов" if self._cent > 0 else ""}"

    def __add__(self, other):
        if isinstance(other, USD):

            sum_whole = self._whole + other._whole
            sum_cent = self._cent + other._cent

            if sum_cent > 99:
                sum_whole += 1
                sum_cent %= 100

            return USD(sum_whole, sum_cent)

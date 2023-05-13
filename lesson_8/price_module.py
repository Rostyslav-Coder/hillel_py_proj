"""This is module of Price class for Home Work 6"""


EXCHANGE_RATE = {
    'EUR -> UAH': 40.313848,
    'EUR -> USD': 1.0909,
    'UAH -> EUR': 0.024805,
    'UAH -> USD': 0.02708,
    'USD -> EUR': 0.9158,
    'USD -> UAH': 36.92
}


class Price:
    """This is Price class"""

    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency


    def _convert_to(self, other) -> float:
        rate = EXCHANGE_RATE[f"{self.currency} -> {other.currency}"]

        return rate


    def _double_convert(self, other):
        rate_1 = EXCHANGE_RATE[f"USD -> {self.currency}"]
        rate_2 = EXCHANGE_RATE[f"USD -> {other.currency}"]
        rate_3 = EXCHANGE_RATE[f"{self.currency} -> USD"]

        return rate_1, rate_2, rate_3


    def __add__(self, other):
        if self.currency == other.currency:
            return Price(round(self.amount + other.amount, 2), self.currency)

        if self.currency == "USD" and other.currency == "UAH":
            rate = self._convert_to(other)
            return Price(
                round(self.amount + other.amount / rate, 2), self.currency
            )

        if self.currency == "USD" and other.currency == "EUR":
            rate = self._convert_to(other)
            return Price(
                round(self.amount + other.amount / rate, 2), self.currency
            )

        if self.currency == "UAH" and other.currency == "USD":
            rate = self._convert_to(other)
            return Price(
                round(self.amount + other.amount / rate, 2), self.currency
            )

        if self.currency == "EUR" and other.currency == "USD":
            rate = self._convert_to(other)
            return Price(
                round(self.amount + other.amount / rate, 2), self.currency
            )

        if self.currency == "UAH" and other.currency == "EUR":
            frst_rate, scnd_rate, thrd_rate = self._double_convert(other)
            return Price(
                round(
                    (self.amount / frst_rate + other.amount / scnd_rate)
                    / thrd_rate,
                    2,
                ),
                self.currency,
            )

        if self.currency == "EUR" and other.currency == "UAH":
            frst_rate, scnd_rate, thrd_rate = self._double_convert(other)
            return Price(
                round(
                    ((self.amount / frst_rate) + (other.amount / scnd_rate))
                    / thrd_rate,
                    2,
                ),
                self.currency,
            )

    def __sub__(self, other):
        if self.currency == other.currency:
            return Price(round(self.amount - other.amount, 2), self.currency)

        if self.currency == "USD" and other.currency == "UAH":
            rate = self._convert_to(other)
            return Price(
                round(self.amount - other.amount / rate, 2), self.currency
            )

        if self.currency == "USD" and other.currency == "EUR":
            rate = self._convert_to(other)
            return Price(
                round(self.amount - other.amount / rate, 2), self.currency
            )

        if self.currency == "UAH" and other.currency == "USD":
            rate = self._convert_to(other)
            return Price(
                round(self.amount - other.amount / rate, 2), self.currency
            )

        if self.currency == "EUR" and other.currency == "USD":
            rate = self._convert_to(other)
            return Price(
                round(self.amount - other.amount / rate, 2), self.currency
            )

        if self.currency == "UAH" and other.currency == "EUR":
            frst_rate, scnd_rate, thrd_rate = self._double_convert(other)
            return Price(
                round(
                    (self.amount / frst_rate - other.amount / scnd_rate)
                    / thrd_rate,
                    2,
                ),
                self.currency,
            )

        if self.currency == "EUR" and other.currency == "UAH":
            frst_rate, scnd_rate, thrd_rate = self._double_convert(other)
            return Price(
                round(
                    ((self.amount / frst_rate) - (other.amount / scnd_rate))
                    / thrd_rate,
                    2,
                ),
                self.currency,
            )

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Wrong Type")

        return Price(self.amount * other, self.currency)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Wrong Type!")
        if other == 0:
            raise ZeroDivisionError("Zero Division Error")

        return Price(self.amount / other, self.currency)

    def __str__(self):
        """print function"""

        return f"{round(self.amount, 2)}: {self.currency}"

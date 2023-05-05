"""This is module of Price class for Home Work 6"""

import requests


class Price:
    """This is Price class"""

    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def _convert_to(self, other) -> float:
        url = (
            "https://www.alphavantage.co/query?"
            "function=CURRENCY_EXCHANGE_RATE&"
            f"from_currency={self.currency}&to_currency={other.currency}&"
            "apikey=O2ZFXGATFZWP5HB5"
        )
        response = requests.get(url, timeout=10).json()
        rate = float(
            response["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        )

        return rate

    def _frst_conv_to_usd(self) -> float:
        url = (
            "https://www.alphavantage.co/query?"
            "function=CURRENCY_EXCHANGE_RATE&"
            f"from_currency=USD&to_currency={self.currency}&"
            "apikey=O2ZFXGATFZWP5HB5"
        )
        response = requests.get(url, timeout=10).json()
        rate = float(
            response["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        )

        return rate

    def _scnd_conv_to_usd(self, other) -> float:
        url = (
            "https://www.alphavantage.co/query?"
            "function=CURRENCY_EXCHANGE_RATE&"
            f"from_currency=USD&to_currency={other.currency}&"
            "apikey=O2ZFXGATFZWP5HB5"
        )
        response = requests.get(url, timeout=10).json()
        rate = float(
            response["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        )

        return rate

    def _convert_from_usd(self) -> float:
        url = (
            "https://www.alphavantage.co/query?"
            "function=CURRENCY_EXCHANGE_RATE&"
            f"from_currency={self.currency}&to_currency=USD&"
            "apikey=O2ZFXGATFZWP5HB5"
        )
        response = requests.get(url, timeout=10).json()
        rate = float(
            response["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        )

        return rate

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
            frst_rate = self._frst_conv_to_usd()
            scnd_rate = self._scnd_conv_to_usd(other)
            thrd_rate = self._convert_from_usd()
            return Price(
                round(
                    ((self.amount / frst_rate) + (other.amount / scnd_rate))
                    / thrd_rate,
                    2,
                ),
                self.currency,
            )

        if self.currency == "EUR" and other.currency == "UAH":
            frst_rate = self._frst_conv_to_usd()
            scnd_rate = self._scnd_conv_to_usd(other)
            thrd_rate = self._convert_from_usd()
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
            frst_rate = self._frst_conv_to_usd()
            scnd_rate = self._scnd_conv_to_usd(other)
            thrd_rate = self._convert_from_usd()
            return Price(
                round(
                    ((self.amount / frst_rate) - (other.amount / scnd_rate))
                    / thrd_rate,
                    2,
                ),
                self.currency,
            )

        if self.currency == "EUR" and other.currency == "UAH":
            frst_rate = self._frst_conv_to_usd()
            scnd_rate = self._scnd_conv_to_usd(other)
            thrd_rate = self._convert_from_usd()
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

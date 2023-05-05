"""This is the main module of Home Work 6"""

from price_module import Price


def add(price: Price) -> Price:
    """This is the adding function"""

    amount = float(input("What`s amount to add: ").strip())
    currency = input("What`s currency: ").upper().strip()
    new_price = Price(amount=amount, currency=currency)
    price += new_price  # type: ignore
    print(f"NEW PRICE IS: {price}")

    return price


def sub(price: Price) -> Price:
    """This is the adding function"""

    amount = float(input("What`s amount for subtraction: ").strip())
    currency = input("What`s currency: ").upper().strip()
    new_price: Price = Price(amount=amount, currency=currency)
    price -= new_price  # type: ignore
    print(f"NEW PRICE IS: {price}")

    return price


def mul(price: Price) -> Price:
    """This is the multiply function"""

    value = float(input("What is the multiplier to multiply: ").strip())
    price *= value  # type: ignore
    print(f"NEW PRICE IS: {price}")

    return price


def div(price: Price) -> Price:
    """This is the divide function"""

    value = float(input("What is the divisor to divide: ").strip())
    price /= value  # type: ignore
    print(f"NEW PRICE IS: {price}")

    return price


def main():
    """This is the main function"""

    amount = float(input("What`s amount of new price: ").strip())
    currency = input("What`s currency: ").upper().strip()
    my_price = Price(amount=amount, currency=currency)

    while True:
        if not (operation := input("Enter an operation (+, -, *, /, p): ")):
            break

        if operation == "p":
            print(f"PRICE IS: {my_price}")
        elif operation == "+":
            my_price = add(my_price)
        elif operation == "-":
            my_price = sub(my_price)
        elif operation == "*":
            my_price = mul(my_price)
        elif operation == "/":
            my_price = div(my_price)
        elif operation == "**":
            print("Unfortunately, money cannot be raised to a power.")


if __name__ == "__main__":
    main()

"""This is the module of Home Work 8"""

import asyncio
from pprint import pprint
from time import perf_counter

import httpx


async def get_rates(from_: str, to_: str):
    """Function to get rates"""
    url = (
        f"https://api.apilayer.com/exchangerates_data/"
        f"convert?to={to_}&from={from_}&amount=1"
    )

    headers = {"apikey": "dtKRZurQqcQaBu11HfSpXScvK4lTcn6P"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        await asyncio.sleep(1)
        content: dict = response.json()
        # print(content)

        rate_dict = {}

        key: str = content["query"]["from"] + " -> " + content["query"]["to"]
        value: float = content["result"]
        rate_dict[key] = value
        print(rate_dict)

        return rate_dict


async def main():
    """Main Functin"""
    CURRENCY = ["USD", "UAH", "EUR"]

    tasks = [
        get_rates(from_=a, to_=b) for a in CURRENCY for b in CURRENCY if a != b
    ]
    data = await asyncio.gather(*tasks)

    pprint(data)


if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(main())
    end = perf_counter() - start
    print(f"Async requests takes {end} seconds")

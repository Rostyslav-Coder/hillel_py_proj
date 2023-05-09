"""This is an Example module"""
# Этот код работает довольно медленно. Измените его, используя многопоточность
# и многопроцессорность, как мы это делали на уроке.

# Добавьте счетчики времени и раскомментируйте команду печати в блоке try/except.
# P.S. Используйте time.perf_counter.

# Шифрование может имитировать тяжелую задачу. Нет необходимости добиваться
# фактического шифрования. +

# Загрузчик изображения должен загрузить изображение по-настоящему. +

import os
import threading
from time import perf_counter, sleep

import requests


# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    """This is encrypt file module"""
    start = perf_counter()
    print(f"Processing text file '{path}' in process {os.getpid()} "
          f"in thread {threading.current_thread().name}")
    # Simulate heavy computation by sleeping for a while
    sleep(2)
    _ = [i for i in range(100_000_000)]
    time_result = perf_counter() - start
    print(f"CPU-bound task taken: {time_result}sec.")


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    """This is download image module"""
    start = perf_counter()
    print(
        f"Downloading image from {image_url} in process {os.getpid()} "
        f"in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url, timeout=5)
    with open("image.jpg", "wb") as file:
        file.write(response.content)
    time_result = perf_counter() - start
    print(f"I/O-bound task taken: {time_result}sec.")


def main():
    """This is main module"""
    try:
        start =perf_counter()
        encrypt_file("rockyou.txt")
        encryption_counter = perf_counter() - start
        download_image("https://picsum.photos/1000/1000")
        download_counter = perf_counter() - start
        total = perf_counter() - start
        print(
        f"Time taken for:\nCPU-bound task: {encryption_counter},\n"
        f"I/O-bound task: {download_counter},\nTotal: {total} seconds"
        )
    except Exception as error:
        print(f"Error occurred: {error}")


if __name__ == "__main__":
    main()

"""This is Multi-processing module of Home Work 7"""

import multiprocessing
import os
import threading
from time import perf_counter, sleep

import requests


# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    """This is encrypt file module"""
    start = perf_counter()
    print(
        f"Processing text file '{path}' in process {os.getpid()} "
        f"in thread {threading.current_thread().name}"
    )
    # Simulate heavy computation by sleeping for a while
    sleep(2)
    _ = [i for i in range(100_000_000)]
    time_result = perf_counter() - start
    print(f"CPU-bound task taken: {time_result}sec.")


# I/O-bound task (downloading image from URL)
def download_image(image_url: str):
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
        start = perf_counter()
        threading_1 = multiprocessing.Process(
            target=encrypt_file, args=("rockyou.txt",)
        )
        threading_2 = multiprocessing.Process(
            target=download_image, args=("https://picsum.photos/1000/1000",)
        )
        threading_2.start()
        threading_1.start()
        threading_1.join()
        encryption_counter = perf_counter() - start
        threading_2.join()
        download_counter = perf_counter() - start
        total = perf_counter() - start
        print(
            f"Time taken for:\nCPU-bound task: {encryption_counter},\n"
            f"I/O-bound task: {download_counter},\nTotal: {total} seconds"
        )
    except Exception as error:
        print(f"Error occurred: {error}")


if __name__ == "__main__":
    start = perf_counter()
    main()
    total = perf_counter() - start
    print(f"TOTAL TIME: {total}sec")

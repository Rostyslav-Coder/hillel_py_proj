"""Module of HOME WORK 3 by Rostyslav P. V-2
Второй вариант, без объявления переменной к которой мог быть
присвоен объект типа генератор. Все донные из функции "find_in_file"
передаются в функцию "new_file_writer" внутри функции "main"
с помощью цикла "for".
"""

from pympler.asizeof import asizeof  # type: ignore


def main():
    """
    This function receives the search word from the user, and passes it to
    the "find_in_file" function along with the name of the file to be searched.
    The words received from the "find_in_file" function are sent to
    the "new_file_writer" function for writing to the file. Then calls the
    "print_file_info" function to display information about the created file.
    """
    word: str = input("What`s word: ").strip().lower()
    for line in find_in_file(word):
        new_file_writer(line)
    print_file_info()


def find_in_file(word: str):
    """
    This function receives the name of the file to search for matches,
    and the search word, returns the results to the "main" function.
    """
    file_name: str = "lesson_3/rockyou.txt"
    with open(file_name, "r", encoding="UTF-8", newline="\n") as file:
        while True:
            line: str = file.readline()
            if not line:
                break
            if word in line.lower():
                yield line


def new_file_writer(line: str):
    """
    This function takes the search results
    and writes them to the file "results.txt".
    """
    file_name = "lesson_3/results.txt"
    with open(file_name, "a", encoding="UTF-8") as new_file:
        new_file.write(line)


def print_file_info():
    """
    This function opens the generated file for reading,
    counts the number of words in the file, and the size of the file.
    Outputs the results to the console.
    """
    with open("lesson_3/results.txt", "r", encoding="UTF-8") as file:
        lines = file.readlines()
        print(f"The number of lines of a cerated file: {len(lines)}")
        size = asizeof(lines)
        print(f"The total size of the created file: {size}")


if __name__ == "__main__":
    main()

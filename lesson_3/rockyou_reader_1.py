"""This is module of HOME WORK 3 by Rostyslav P. V-1
Первый вариант, с обявлением переменной к которой присваивается
объект типа генероатор и последующей записью в тхт файл с помощю
второго "генератора", во втором я не уверен.
"""

from pympler.asizeof import asizeof  # type: ignore


def main():
    """
    This function receives the search word from the user and
    passes it to the "find_in_file" function. The words found in
    the text file using the "find_in_file" function are collected
    in the "generator" and then sent to the "new_file_writer" function
    to be written to the text file. The "print_file_info" function
    is then called to display information about the created text file.
    """
    word = input("What`s word: ").strip().lower()
    my_generator = find_in_file(word)
    new_file_writer(my_generator)
    print_file_info()


def find_in_file(word):
    """
    This function takes the search word, looks for matches in
    a text file, and returns the search results to the "main" function.
    """
    file_name = "lesson_3/rockyou.txt"
    with open(file_name, "r", encoding="UTF-8", newline="\n") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if word in line.lower():
                yield line


def new_file_writer(my_generator):
    """
    This function takes the results of search
    and writes them to the file "results.txt".
    """
    file_name = "lesson_3/results.txt"
    with open(file_name, "a", encoding="UTF-8") as new_file:
        new_file.writelines(line for line in my_generator)


def print_file_info():
    """
    This function opens the "results.txt" file for reading,
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

import os


def get_file_list():
    path = os.getcwd() + "\\files"
    dir_list = os.listdir(path)
    ct = 0
    for doc in dir_list:
        ct += 1
        txt_file = doc
        print(f"{ct}. {txt_file}")
    selection = int(input("Please select which file you wish to open: "))
    file_name = dir_list[selection - 1]
    return file_name


def write_to_file(key, string):
    path = os.getcwd() + "\\files"
    file_name = str(input("Please name your file: (Example: file_name) ")) + ".txt"
    with open(f"{path}\\{file_name}", "a+") as file:
        file.write(key + ":" + string)


def read_from_file(file_name):
    path = os.getcwd() + "\\files"
    with open(f"{path}\\{file_name}", "r+") as file:
        lines = file.readlines()
    x_string = "".join(lines)
    split_list = x_string.split(":")
    key = split_list[0]
    string = split_list[1]
    print(key + "\n" + string)
    return key, string

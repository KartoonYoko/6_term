# from fileFunctions import *
import sys
from database import *
from log_func import *

# TODO Возможности админа
#   - изменять мод у файлов
#   - создавать группы пользователей
#   - объеденять в группы пользователей
#   - смотреть лог сервера (в отдельном файлике)

FIRST_DIR = "storage"
COMMON_GROUP = "common"


def get_path(arr=""):
    """
        Формирует путь из массива каталгов
    :param arr:
    :return string:
    """
    if path:
        if arr == '..':
            path.pop()
        pathname = ''
        for key in path:
            pathname = os.path.join(pathname, key)
        if arr:
            pathname = os.path.join(pathname, arr)
        pathname = pathname.replace('\\', '/')
        return pathname
    else:
        return FIRST_DIR


def show_directory(dirpath):
    CWD = get_path()
    if not dirpath:
        pathname = os.path.abspath(os.path.join(CWD, '.'))
    elif dirpath.startswith(os.path.sep):
        pathname = os.path.abspath(dirpath)
    else:
        pathname = os.path.abspath(os.path.join(CWD, dirpath))
        path.append(dirpath)

    if not os.path.isdir(pathname):
        fileMessage = fileProperty(pathname)
        print(fileMessage)
    else:
        for file in os.listdir(pathname):
            fileMessage = fileProperty(os.path.join(pathname, file))
            print(fileMessage)


def get_help(arg):
    if arg:
        desc = commands_list.get(arg)[1]
        if not desc:
            print("no such command", desc)
        else:
            print(arg, ": ", desc)
    else:
        for key in commands_list:
            print(key, ": ", commands_list.get(key)[1])


def parse_input(str):
    space_pos = str.find(' ', 0)
    if space_pos == -1:
        return str, ''
    command = str[:space_pos]
    arg = str[space_pos + 1:]
    if arg.find(' ', 0) != -1:
        arg = arg.split()
    return command, arg


def change_mode(arg):
    CWD = get_path()    # mode test.jpg
    rules = 'rwx'
    group = COMMON_GROUP
    if type(arg) == list:
        rules = arg[2]  # rules rwx
        group = arg[1]  # group name
        arg = arg[0]    # file name
    filepath = os.path.abspath(os.path.join(CWD, arg))
    if not os.path.exists(filepath):
        print("file doesnt exist")
        return
    ftp_db.set_rules_to_file_for_group(group, filepath, rules)


def get_groups(arg):
    res = ftp_db.get_list_groups()
    if res:
        print(res)


def get_users(arg):
    print(ftp_db.get_all_users())


def set_user_group(arg):
    """
    задаст группу пользователю, если группы нет - создаст ее
    """
    name = arg[0]
    group = arg[1]
    ftp_db.set_group_to_user(name, group)


def get_files(arg):
    print(ftp_db.get_files_list())


def quit(arg):
    sys.exit()


if __name__ == "__main__":
    commands_list = {
        "list": [show_directory, "[dirpath] shows info file or catalog and moves to one"],
        "help": [get_help, "list of commands"],
        "mode": [change_mode, "[file, group, mode] change file mode for group (rwx)"],
        "groups": [get_groups, "get all groups"],
        "users": [get_users, "get all users"],
        "files": [get_files, "get all files"],
        "usergroup": [set_user_group, "[username , group] set group to user, "
                                      "if there is not the group, ones will be made"],
        "quit": [quit, "close terminal"],
        "q": [quit, "close terminal"]
    }
    ftp_db = DatabaseFTP(FIRST_DIR, "FTP_server_bd.db")
    path = [FIRST_DIR]          # PATH of current directory
    print("Enter command, to get help enter HELP")
    user_input = ''
    while user_input != 'q':
        user_input = input(">>> ").lower()
        command, arg = parse_input(user_input)
        func = commands_list.get(command)
        if func:
            func[0](arg)
        else:
            print("not recognized command")

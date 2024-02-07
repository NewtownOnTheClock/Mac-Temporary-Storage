import os
import datetime as dt
import shutil

source_dir = "YOUR PATH"
trash_dir = os.path.expanduser('~/.Trash')


def list_file():
    dir_list = os.listdir(source_dir)
    return dir_list


def date_last_modified():
    file_lst = list_file()
    file_path = [f"{source_dir}/{i}" for i in file_lst]
    file_datem = {path: dt.datetime.fromtimestamp(os.path.getmtime(path)) for path in file_path}
    return file_datem


def date_today():
    return dt.datetime.now()


def main():
    now = date_today()
    two_days_ago = now - dt.timedelta(days=2)

    file_date_dict = date_last_modified()

    for (k, v) in file_date_dict.items():
        if two_days_ago > v:
            shutil.move(k, trash_dir)


if __name__ == '__main__':
    main()


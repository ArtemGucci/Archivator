import os
import shutil
from datetime import datetime

TYPES = {'bztar': '.tar.bz2', 'gztar': '.tar.gz', 'xztar': '.tar.xz', 'tar': '.tar', 'zip': '.zip'}


def make_reserve_arc(source, dest, archive_type):
    time = datetime.today()
    time = [time.year, time.month, time.day, time.hour, time.minute, time.second]
    name = 'archive_' + '_'.join(map(str, time))
    shutil.make_archive(name, archive_type, root_dir=source)
    if dest == os.getcwd():
        return name
    shutil.move(os.getcwd() + '/' + name + TYPES[archive_type], dest)
    return name


def main():
    while True:
        source = input('Введите полный путь к начальному каталогу.')
        if not os.path.exists(source):
            print('Увы, путь указан неверно.')
            print()
            continue
        dest = input('Введите полный путь к конечному каталогу.')
        if not os.path.exists(dest):
            print('Увы, указанный путь либо не существует, либо не подходит для копирования.')
            print()
            continue
        break

    print()
    archive_type = 'zip'
    archives = ['bztar', 'gztar', 'tar', 'xztar', 'zip']
    print('Виды поддерживаемых архивов:')
    print(', '.join(archives))
    print()

    while True:
        user_type = input('''Введите тип архива, в который поместятся данные.
Он должен быть в списке перечисленных архивов. По умолчанию будет zip, тогда нажмите Enter.''')
        if user_type:
            if user_type in archives:
                print('Архив успешно выбран.')
                archive_type = user_type
                break
            print('Увы, но данный архив не поддерживается, либо вы ввели его неправильно.')
            print()
        else:
            break

    print()
    print('Ожидайте, архив создаётся.' + '\n')
    name = make_reserve_arc(source, dest, archive_type)
    print(f'Архив с именем {name} успешно создан.')


main()

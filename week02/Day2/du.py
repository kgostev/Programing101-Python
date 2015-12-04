import os
import sys


def main():
    try:
        if os.path.isdir(sys.argv[1]):
            size = calculate_size(sys.argv[1])
            print(sizeof_fmt(size))
        else:
            size = os.path.getsize(sys.argv[1])
            print(sizeof_fmt(size))
    except FileNotFoundError as error:
        print(error)


def calculate_size(files):
    sum_ = 0
    for root, dirs, files, rootfd in os.fwalk(files):
        sum_ += sum([os.stat(name, dir_fd=rootfd).st_size for name in files])
    return sum_


def sizeof_fmt(num):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, 'B')
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', 'B')

if __name__ == '__main__':
    main()

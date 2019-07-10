import os

import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def treewalker(start):
    total_files = 0
    total_size = 0

    for root, dirs, files in os.walk(start):
        file_size = sum(os.path.getsize(os.path.join(root, file_or_dir)) for file_or_dir in files) # noqa E501
        file_count = len(files)

        total_size += file_size
        total_files += file_count

        print(f"{root} has {file_size:n} bytes in non-directory files")
    print(f"{start} contains {total_files:n} total files with a combined size of {total_size:n} bytes") # noqa E501


# treewalker("env")
treewalker(os.path.join(os.getcwd(), "..", "..", "..", "The Profit"))

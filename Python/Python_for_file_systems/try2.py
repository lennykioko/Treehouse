import os


def dir_contains(path, search_files):
    scanner = os.scandir(path)
    existing_files = set(file.name for file in scanner)
    search_files = set(search_files)
    print(f"{existing_files}\n{search_files}")
    if search_files <= existing_files:
        return True
    return False


print(dir_contains(os.getcwd(), ["tree.py", "try.py", "try2.py", ".env"]))

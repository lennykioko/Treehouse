import os
import pathlib

# print(os.getcwd())
# /Users/lennykioko/Desktop/Treehouse/Python/Python_for_file_systems

# print(os.path.isabs('/Users/lennykioko/Desktop/Treehouse/Python/Python_for_file_systems'))
# True

# print(os.path.join(os.getcwd(), 'env'))
# /Users/lennykioko/Desktop/Treehouse/Python/Python_for_file_systems/env

# mind you path dos not check if the path is valid, it just constructs the path
# print(os.path.join(os.getcwd(), '..')) # moving one step back

# you can add multiple paths
# print(os.path.join(os.getcwd(), '..', 'Tkinter'))

path = pathlib.PurePath(os.getcwd())

path2 = path / 'env' / 'bin'  # pathlib overides the / from being a division sign

# print(path, path2, sep='\n')

# print(path2.root)
# print(path2.parts)
# print(path2.parents[3])

path3 = path2 / 'activate_this.py'

# print(path3.name)
# print(path3.suffix)

# print(os.listdir())
# print(os.listdir(path2))

# print(list(os.scandir()))

# scanner = os.scandir()
# files = list(scanner)
# print(files[0])
# print(files[0].is_file())
# print(files[0].stat())
# scanner.close()

# print(os.walk(os.getcwd())) # is a generator

# print(os.path.exists("trying"))

# # creates the file since you opened it in append or write mode
# open("trying/testing.txt", "a").close()

# mknod works on Windows and Linux, in mac you have to run Python in sudo mode
# os.mknod("trying/success.txt")

# creates a single directory
# os.mkdir("trying/mkdir")

# raises an error if directory already exists
# os.makedirs("trying/makedirs/templates/platform/mobile/android")

# ignores error if directory already exists
# os.makedirs("trying/makedirs/templates/platform/mobile/android", exist_ok=True)

# single file/directory
# os.rename("trying", "experiments")

# os.makedirs("experiment2/attempts/nothing")

# os.rename("experiment2", "experiments/renaming/something")

# renames the directory and moves it into another existing folder
# os.rename("experiment2", "experiment/something")

# renames can create folders and therefore can work with folders that do not already exist
# os.renames("experiment/something", "experiment/potential/sm_awesome")

# to avoid potential cross-platform isuues with os.renames() let's use os.replace()
# os.replace("experiment/potential", "experiment/renaming")

# open("nonsense.txt", "a").close()

# deletes a file, if file still in use, Windows will throw an error
# os.remove("nonsense.txt")

# os.mkdir("empty")

# only deletes empty directories
# os.rmdir("empty")

# delete several directories, the directories need to be empty to be deleted
# os.removedirs("path/to/directories")


# all the above permanently delete files, to send to trash use:
from send2trash import send2trash

send2trash("experiment/del.txt")

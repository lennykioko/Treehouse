import os

allfiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))] # noqa E501


for file in allfiles:
    append = ""
    new_file_name = "{}--{}.mp4".format(append, file)
    prev = os.path.join(os.getcwd(), file)
    new = os.path.join(os.getcwd(), new_file_name)

    os.rename(prev, new)

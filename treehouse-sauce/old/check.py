import os

PATH = '.'

folders = [
    fol for fol in os.listdir(PATH)
    if os.path.isdir(fol)
]
print(folders)

for fol in folders:
    if os.path.exists(fol) and os.path.isdir(fol):
        if not os.listdir(fol):
            print(f"Empty: {fol}")
        else:
            pass
    else:
        print(f"Doesn't exist: {fol}")

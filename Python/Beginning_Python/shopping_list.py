import os


shopping_list = []

def clear_screen():
    # run the cls script if on windows and clear if on Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")


def add_to_list(item):
    shopping_list.append(item)
    print("\nAdded: List now has {} items".format(len(shopping_list)))
    show_list()


def show_list():
    clear_screen()
    print("\nMy shopping list: {}".format(", ".join(shopping_list)))


def show_help():
    clear_screen()
    print("\nWhat should you pick from the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to display your current shopping list.

    """)


show_help()

while True:
    new_item = input("> ")

    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
        break

    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    else:
        add_to_list(new_item)

show_list()

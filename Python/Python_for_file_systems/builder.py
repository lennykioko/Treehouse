# incomplete, refer to treehouse for the complete builder.py

import pathlib


def get_root():
    root = pathlib.PurePath(
        input("What's the full path where you'd like the project? ")
    )
    if not root.is_absolute():
        return get_root()  # we recall the function till we get what we want
    return root


def main():
    """Application Entrypoint"""
    project_root = get_root()
    project_name = None

    while not project_name:
        project_name = input("What's the name of the project? ").strip()

    print(f"creating {project_name} in {project_root}")

if __name__ == "__main__":
    main()

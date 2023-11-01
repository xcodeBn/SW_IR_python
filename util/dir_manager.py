import os


def get_directory(default_dir):
    while True:
        user_directory = input(
            f"Enter a directory path or press Enter to use the default directory '{default_dir}': ").strip()

        if not user_directory:
            return default_dir

        if os.path.isdir(user_directory):
            return user_directory
        else:
            print("The entered path does not exist or is not a directory. Please enter a valid directory path.")

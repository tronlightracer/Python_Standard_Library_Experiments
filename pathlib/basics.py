#! /home/trev/.pyenv/shims/python3

from pathlib import Path
from os import chdir

def main():
    print(f"Current working directory: {Path.cwd()}")
    print(f"Home Directory: {Path.home()}")
    # use '/' to create new paths with the Path object
    path_obj = Path("/opt") / "k8s" 
    # checks whether the file path exists
    print(path_obj)

    path2 = Path("basics.py")
    # necessary to get the parent folder
    full_path = path2.resolve()
    print(f"Parent path: {full_path.parent}")

    # get the parent above the current parent by calling parent twice
    print(f"Grand parent: {full_path.parent.parent}")

    # to grab the stem of the file name:
    print(f"Stem: {full_path.stem}")

    # to grab the file extension name
    print(f"Suffix: {full_path.suffix}")

    # checks whether the file is a directory or not with the is_dir() function
    print(f"Is this a directory?: {full_path.parent.is_dir()}")

    # checks whether the path is a file or not with the is_file function
    print(f"Is this a file?: {full_path.is_file()}")

    # create a new file with pathlib
    new_file = Path.cwd() / "new_file.txt"
    new_file.touch()
    print(f"new_file: {new_file}")

    # write text to the new file
    new_file.write_text("Hello")

    # to delete the new_file.txt
    new_file.unlink()


    # create a new directory
    try:
        new_dir = Path.cwd() / "new_dir"
        new_dir.mkdir()
        # changing a directory with os.chdir()
        print(f"New directory: {new_dir}")
        chdir(new_dir)
        print(f"Current working directory: {Path.cwd()}")
    except FileExistsError:
        # removing a directory
        new_dir.rmdir()

if __name__ == '__main__':
    main()
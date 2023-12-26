# write a script to remove all the input.txt and test.txt files in all the days

import os
import shutil

if __name__ == "__main__":
    top = os.getcwd()
    # print("removing all input.txt and test.txt files")
    for root, dirs, files in os.walk(top, topdown=False):
        for file in files:
            if file == "input.txt" or file == "test.txt":
                os.remove(os.path.join(root, file))
                print(f"removed {os.path.join(root, file)}")
        for dir in dirs:
            if dir == "__pycache__":
                shutil.rmtree(os.path.join(root, dir))
                print(f"removed {os.path.join(root, dir)}")

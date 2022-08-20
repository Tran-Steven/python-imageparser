import os
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

# Popup pick directory with tkinter to file path to edit images ( will not go through subdirectories )
def search_for_file_path():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(
        parent=root, initialdir=currdir, title="Please select a directory:"
    )
    if len(tempdir) > 0:
        print("You chose: %s" % tempdir)
    return tempdir


print("Choose your directory")
file_path = search_for_file_path() + "/"
root.destroy()


# Loop until all specified items are deleted (if yes)
user_input = input("Do you want to remove your files? (y/yes) (n/no)")
if user_input in ["y", "Y", "yes", "Yes", "YES"]:
    for file_name in os.listdir(file_path):

        source = file_path + file_name

    # In this case, because I have images with a set pattern e.g ( File_0.jpg, File_1.jpg, Icon_0.jpg, Icon_1.jpg)
    # I only want to keep files with _0, so if they do not contain _0, then the file is removed.
    if "_0" in file_name:
        print("Correct file")
    else:
        os.remove(source)
if user_input in ["n", "no", "No", "N"]:
    print("No files were removed")

# Option to rename file, upper,lower, and replace _0
user_input = input("Do you want to rename your files? (y/yes) (n/no)")
if user_input in ["y", "Y", "yes", "Yes", "YES"]:

    # functions that put all files upper/lower case (with respect to ".")
    def toUpper(file_name):
        formatText = file_name.split(".")
        return formatText[0].upper() + "." + formatText[1]

    def toUnder(file_name):
        formatText = file_name.split(".")
        return formatText[0].under() + "." + formatText[1]

    user_input = input(
        "Do you want it all uppercase or lowercase? (u/upper) (l/lower) (n/none)"
    )
    if user_input in ["u", "upper", "Upper", "U"]:
        for file_name in os.listdir(file_path):
            source = file_path + file_name
            os.rename(source, toUpper(file_name))
            print("Uppercase renaming success")
    if user_input in ["l", "lower", "Lower", "L"]:
        for file_name in os.listdir(file_path):
            source = file_path + file_name
            os.rename(source, toUnder(file_name))
            print("Lowercase renaming success")
    if user_input in ["n", "none", "None", "N"]:
        print("No upper or under were made")
    user_input2 = input("remove _0 ? (y,yes) (n/no)")
    if user_input2 in ["y", "Y", "yes", "Yes", "YES"]:
        for file_name in os.listdir(file_path):
            source = file_path + file_name
            target = file_name.replace("_0", "")
            os.rename(source, target)
            print("removed _0 successfully")
    if user_input2 in ["n", "no", "No", "N"]:
        print("done")

if user_input in ["n", "no", "No", "N"]:
    print("Program ending...")

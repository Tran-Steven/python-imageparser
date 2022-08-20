import os


# Insert full file path to the directory with the images ( will not go through subdirectories )
file_path = "/Users/steventran/Desktop/imageparser/"

# loops until all files are gone through


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
    print("no files were removed")

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
        "Do you want it all uppercase or lowercase? (upper) (lower) (none)"
    )
    if user_input == "upper":
        for file_name in os.listdir(file_path):

            source = file_path + file_name
            os.rename(source, toUpper(file_name))
            print("upper success")
    if user_input == "lower":
        for file_name in os.listdir(file_path):

            source = file_path + file_name
        os.rename(source, toUnder(file_name))
        print("lower success")
    if user_input == "none":
        print("No upper or under were made")

    user_input2 = input("remove _0 ? (y,yes) (n/no)")
    if user_input2 in ["y", "Y", "yes", "Yes", "YES"]:
        for file_name in os.listdir(file_path):

            source = file_path + file_name
            target = file_name.replace("_0", "")
            os.rename(source, target)
        print("removed _0")
    else:
        print("done")
if user_input in ["n", "no", "No", "N"]:
    print("no files were renamed, program end")
else:
    print("unknown command")

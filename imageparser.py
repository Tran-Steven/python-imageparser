import os

# Insert full file path to the directory with the images ( will not go through subdirectories )
file_path = '/Users/pyUser/Images/'

# loops until all files are gone through
for file_name in os.listdir(file_path):

    source = file_path + file_name

# In this case, because I have images with a set pattern e.g ( File_0.jpg, File_1.jpg, Icon_0.jpg, Icon_1.jpg)
# I only want to keep files with _0, so if they do not contain _0, then the file is removed.
    if "_0" in file_name:
       print("Correct file") 
    else:
        os.remove(source)

# Python-imageparser
A small Python script that removes files from a directory, made for use in [League of Wordle](https://github.com/Tran-Steven/leaguewordle) but customizable to fit your own needs.

## file_path 
Can either use absolute or relative path depending on where you are running the script.

## file_name
Loops through all of the files in the directory. ( does not go through subdirectories )

## if statement
Changeable to your needs, in my case, I had files with a set pattern e.g ( File_0.jpg, File_1.jpg, Icon_0.jpg, Icon_1.jpg)
If the file name does not contain "_0", then the script runs `os.remove(source)` which removes the file.

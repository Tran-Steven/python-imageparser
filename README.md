# Python-imageparser
A simple Python script that removes files from a directory, made for use in [League of Wordle](https://github.com/Tran-Steven/leaguewordle) but customizable to fit your own needs.

## file_path 
Select the file path to your folder with the Directory popup.

## file_name
Loops through all of the files in the directory. ( does not go through subdirectories )

## Removing Files
At the moment, if you select Yes to deleting files, it deletes files that does not contain "_0" in the file name. This is due to the script's use in my other project listed above. But it is customizable to fit your own needs or uses.

## Renaming Files
The script can rename all the files in the folder to be all Uppercase or Lowercase.

The last renaming option is specific to my other project that removes "_0" from the file name.

The script keeps the file extension as the file name gets "split" having the "." as the anchor. This makes it so the script stops before the file extension and only runs until the end of the file name. 

*issues may occur if files have more than one "." in its name*

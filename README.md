# Rename Files with American Style Dates to European Style Dates

A program to automate a boring task like changing American style dates (MM-DD-YYYY) to European style dates (DD-MM-YYYY).

Rather than the doing it one by one which would numb the brain you write a program to changes hundreds if not thousands of them.

The concept can be adapted to any number of other uses.

## What It Does

* searches all filenames in current working directory for American style dates

* when one is found, renames the file with the month and day swapped to make it European style

## Code Should Do

* create regex that can ID the text pattern of American style dates

* call `os.listdir()` to find all the files in the working directory

* cycle over each filename, using regex to check whether it has a date

* if it has a date, rename the file with `shutil.move()`

## Example Filenames Targeted

target...

spam4-4-1984.txt

01-03-2014eggs.zip

ignore...

littlebrother.epub

## References

folder:  renameDates_021618_1

execution file:  renameDates_021618_1.py

ABSP:  335
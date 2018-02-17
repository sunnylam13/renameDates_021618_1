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

## Challenges

### Saturday, February 17, 2018 2:09 PM

Dates have a lot of special exceptions that are certainly annoying.

The regex pattern:

	datePattern = re.compile(r'''
			^(.*?) # all text before the date
			((0|1)?\d)- # one or two digits for the month
			((0|1|2|3)?\d)- # one or two digits for the day
			(\d{4}) # four digits for the year
			(.*?)$ # all text after the date
		''', re.VERBOSE)

will catch the majority of cases.

While years like 1785 is valid, the regex pattern can use just 20 and 21st century to avoid accidentally matching nondate filenames with a date-like format...

i.e.  11-12-2000.txt

## Additional Uses or Derivations

This program can be adapted to do things like...

* add a prefix to file names

* change filenames with Euro dates to American dates instead

* remove zeros from files like `photo0056.jpg`

etc...

## References

folder:  renameDates_021618_1

execution file:  renameDates_021618_1.py

ABSP:  335

### Regex

The registry expressions used in the program or variants during the creation process.

https://regexr.com/3ku5m

	^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-(\d{4})(.*?)$

https://regexr.com/3kupi

	^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$


# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# USAGE
# xxxx

import shutil, os, re

#####################################
# REGEX
#####################################

# create a regex that matches files with the American date format

datePattern = re.compile(r'''
		^(.*?) # all text before the date
		((0|1)?\d)- # one or two digits for the month
		((0|1|2|3)?\d)- # one or two digits for the day
		((19|20)\d\d) # four digits for the year
		(.*?)$ # all text after the date
	''', re.VERBOSE)

#####################################
# END REGEX
#####################################

#####################################
# FILE COMPILE
#####################################

# Loop over the files in the working directory

for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilename)

	# skip files without a date
	
	if mo == None:
		continue # skip the rest of the loop and move onto the next filename

	# get the different parts of the filename
	# the groups are in the order of () in the regex statement used (see `datePattern` in REGEX)
	# parts are used to form the European style filename
	# see notes on "Nested Brackets of Groups" on counting brackets (python-notes-051416/regex-py3-090317-1.md)
	
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

#####################################
# END FILE COMPILE
#####################################


#####################################
# FILE PROCESSING
#####################################

# form the European style filename



# get the full, absolute file paths


# rename the files

#####################################
# END FILE PROCESSING
#####################################


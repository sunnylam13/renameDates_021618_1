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

# TODO:  Loop over the files in the working directory
# TODO:  skip files without a date
# TODO:  get the different parts of the filename
# TODO:  form the European style filename
# TODO:  get the full, absolute file paths
# TODO:  rename the files


# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# USAGE
# xxxx

import shutil, os, re

#####################################
# REGEX
#####################################

# create a regex that matches files with the American date format
# Reference
# https://regexr.com/3ku5m
# ^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-(\d{4})(.*?)$

datePattern = re.compile(r'''
		^(.*?) # all text before the date
		((0|1)?\d)- # one or two digits for the month
		((0|1|2|3)?\d)- # one or two digits for the day
		(\d{4}) # four digits for the year
		(.*?)$ # all text after the date
	''', re.VERBOSE)

#####################################
# END REGEX
#####################################


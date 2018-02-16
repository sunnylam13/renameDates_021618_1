# Scratch File

## Friday, February 16, 2018 4:08 PM

folder:  renameDates_021618_1

## Regex Test

### Friday, February 16, 2018 4:54 PM

https://regexr.com/3ku5m

spam4-4-1984.txt

01-03-2014eggs.zip

16-01-1982.bat # this one should not be selected at all

A program to automate a boring task like changing American style dates (MM-DD-YYYY) to European style dates (DD-MM-YYYY).

remove everything after "spam4-4-1984.txt" including spaces and returns and the formula `^((.*)?)((0|1)?\d)-((0|1|2|3)?\d)-(\d{4})((.*)?)$` will work...

further shortened...

	^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-(\d{4})(.*?)$
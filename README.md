# Phone Number and Email Address Extractor

*NOTE: This example comes from the book Automating The Boring Stuff With Python*

## Project is as follows:
Create a program to find every phone number and email address in a long web page or document. Replace the text on the clipboard with just the phone numbers and emial adderesses it finds.

**The program needs to do the following:**
* Get the text off the clipboard
* Find all phone numbers and email addresses in the text.
* Past them onto the clipboard

**Steps used for the program:**
* Use the ```pyperclip``` module to copy and paste strings.
* Create two regexes, one for matching phone numbers and the other for matching email addresses.
* Find all matches, not just the first match, of both regexes.
* Neatly format the matches strings into a single string to paste.
* Display some kind of message if no matches were found in the text.

**Ideas for Similar Programs:**
* Find website URLs that begins with *http://* or *https://*
* Clean up dates in different date formats (such as 3/14/15, 03-14-15, and 2015/3/14) by replacing them with dates in a single, standard format.
* Remove sensitive information such as Social Security or credit card numbers.
* Find common typos sucha as multiple  spaces between  words, accidentally accidentally repeated words, or multiple exclamation marks at the end of sentences. Those are annoying!!

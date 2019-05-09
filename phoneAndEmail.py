#! Python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard
import pyperclip, re

# Create phone number regex
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?              # Area code
(\s|-|\.)?                      # Separator
(\d{3})                         # First 3 digits
(\s|-|\.)                       # Separator
(\d{4})                         # Last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension
)''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+          # Username
@                          # @ symbol
[a-zA-Z0-9.-]+             # Domain name
(\.[a-zA-Z]{2,4})          # Dot-something
)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = [] # Store the matches found

for groups in phoneRegex.findall(text):
    # phoneNum contains a string built from groups 1, 3, 5 and 8 of the matched text
    # These groups are the area code, first three digits, last four digits, and extension
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
# Append group 0 of each match to get the entire regular expression 
for groups in emailRegex.findall(text):
    matches.append(groups[0])
# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

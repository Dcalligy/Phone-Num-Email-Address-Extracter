#! Python3
# phoneAndEmail.py - Finds website URLs that begin with http:// or https://
import pyperclip, re

# TODO: Figure out how to get the rest of the path to show i.e.,(anything after the URL extension)
# Create http/https regex
urlRegex = re.compile(r'''(
(https?://)         # Checks for http:// or https:// protocol
[a-zA-Z0-9._%+-/]+  # Domain name
(\.[a-zA-Z]{2,6})   # URL extension
)''', re.VERBOSE)

# Find matches of text
text = str(pyperclip.paste())
matches = [] # Store the the matches found

# Append group[0] index of each match to retrieve the entire regex
for groups in urlRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard and display output
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No URL protocol was found.')
import re
from datetime import datetime

dates = ['3/4/2015', '03-14-2015', '10/02/09', '07/22/09', '09-08-2008', '9/9/2008', '11/4/2010', '03-07-2009', '09/01/2010']

datesRegex = re.compile(r'''
\s*      # Optional whitespace
(\d+)    # Month
[-/]     # Separator
(\d+)    # Day
[-/]     # Separator
(?:20)?  # Sentury (optional)
(\d+)    # Years (YY)
\s*      # Optional whitespace
''', re.VERBOSE)

numDates = [datesRegex.sub(r'\1/\2/20\3', date) for date in dates]
# We can format the create multiple versions of formatDates to work with other date formats.
formatDates = [datetime.strftime(datetime.strptime(date, '%m/%d/%Y'), '%m/%d/%Y') for date in numDates]
print(formatDates)
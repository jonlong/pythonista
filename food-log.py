# coding: utf-8

import sys
import json
import clipboard
import pydash
from datetime import datetime, date, time

date_format = '%Y-%m-%d'
raw_drafts_entry = sys.argv[1].split('\n')
entries = []

#json_string = clipboard.get()

json_string = '[{"date":"2016-01-21","entries":[{"time":"2013-02-21 06:45:45.658505","foods":["food 1","food 2","food 3"]},{"time":"2013-02-21 06:55:45.658505","foods":["food 4","food 5","food 6"]}]}]'

# parse the JSON file
try:
	data = json.loads(json_string)

# throw an error for Workflow if JSON parsing fails
except ValueError:
	print "The JSON data in food-log.json is invalid."
	sys.exit(1)
	
# see if there's a record for today's date already by returning the index (if it's -1, it doesn't exist yet)
todays_entry_index = pydash.find_last_index(data, lambda x: datetime.strptime(x['date'], date_format).date() == date.today())

# if there's not a record for today
if todays_entry_index == -1:
	
	# Add a record for today's date
	data.append({'date': date.today().strftime(date_format), 'entries': []})
	
	# update todays_entry_index
	todays_entry_index = len(data) - 1
	
# build our entries with the food list from Drafts
for line in raw_drafts_entry:
	entries.append(line)
	
# add today's entries
data[todays_entry_index]['entries'].append(entries)

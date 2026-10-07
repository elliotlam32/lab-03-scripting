#!/usr/bin/python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

print(GHUSER)
print(url)

def retrieve_events(url1):
	"""This function donwloads data from the url, and passes the JSON data is acquires into a normal python list/dict"""
	print('running retrieve_events')
	urldata = requests.get(url1).text
	pylist = json.loads(urldata)
	return pylist

def print_events(event, n=5):
	"""This funciton prints n items from the list events"""
	print('running print_events')
	for x in event[:n]:
		event = x['type'] + ' :: ' + x['repo']['name']
		print(event)

def main():
	"""retrieve and print github information"""
	print('running main')
	print(GHUSER)
	print(url)
	blah=retrieve_events(url)
	print_events(blah)

if __name__ == "__main__":
	main()

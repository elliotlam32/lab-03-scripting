#!/usr/bin/python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

print(GHUSER)
print(url)

def retrieve_events(url1):
	print('running retrieve_events')
	"""This function donwloads data from the url, and passes the JSON data is acquires into a normal python list/dict"""
	urldata = requests.get(url1).text
	pylist = json.loads(urldata)
	return pylist

def print_events(event, n=5):
	print('running print_events')
	"""This funciton prints n items from the list events"""
	for x in event[:n]:
		event = x['type'] + ' :: ' + x['repo']['name']
		print(event)

def main():
	print('running main')
	"""retrieve and print github information"""
	print(GHUSER)
	print(url)
	blah=retrieve_events(url)
	print_events(blah)

if __name__ == "__main__":
	main()

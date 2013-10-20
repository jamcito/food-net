#!/usr/bin/env python

import json

datafile = "debug20.json"

def main():
	with open(datafile) as f:
		lines = [json.loads(line) for line in f]
		print lines[0]['ingredients']


if __name__ == '__main__':
	main()
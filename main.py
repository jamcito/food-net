#!/usr/bin/env python

from sqlalchemy import *
import json


datafile = "debug20.json"

user = 'postgres'
# password = ''
host = 'localhost'
dbname = 'food'
dbstring = 'postgresql://' + user + ':' + password + '@' + host + '/' + dbname


def fetchjson():
	with open(datafile) as f:
		lines = [json.loads(line) for line in f]
		# print lines[0]['ingredients']
		print len(lines), 'records read'
		print lines[0]
		return lines


def populate(records):
	print len(records), 'records to populate'
	db = create_engine(dbstring)
	metadata = MetaData(db)
	recipes = Table("recipes", metadata, autoload=True)
	run(recipes.select())



def run(stmt):
    rs = stmt.execute()
    for row in rs:
        print row


if __name__ == '__main__':
	records = fetchjson()
	populate(records)
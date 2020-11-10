#!/usr/bin/env python
import pypwned, os, json, sys, time

pwny = pypwned.pwned("HBIP_API_KEY")

filepath = sys.argv[1]
with open(filepath) as fp:
	for line in fp:
		line = line.strip()
		time.sleep(3)
		result = pwny.getAllBreachesForAccount(email=line)
		f = open("output.log", "a")
		f.write(str(line)+","+str(result)+"\r\n")
		f.close()

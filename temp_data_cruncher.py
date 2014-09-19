#!/usr/bin/python

import sys

months = {}

def main():
	# loops over input arguments and creates month dicts to be stored in months
	for x in sys.argv:
		if x == "temp_data_cruncher.py":
			continue
		else:
			month = argv[x]
			months[name] = month
			months[value] = monthCreate(month)
			
	# calculate mean and deviance
	for month in months:
		month["max_mean"] = mean(month["max"])
		month["min_mean"] = mean(month["min"])
		three_degrees(month)

	# output shit
	for month in months:
		print month['name'] + "\nMax Mean: " + month["max_mean"] + "\nDeviants: "
		for i in month['maxdev']:
			print i
		print "\nMin Mean: " + month["min_mean"] + "\nDeviants: "
		for i in month['mindev']:
			print i
		
def monthCreate(month):
	month_dict["name"] = month
	
	# makes list entries for month temp data
	month_max = open(month + "_max.txt", 'r')
	month_dict["max"] =[]
	for line in month_max:
		month_dict["max"].append(int(line.strip('\n')))
	
	month_min = open(month + "_min.txt", 'r')
	month_dict["min"] = []
	for line in month_min:
		month_dict["min"].append(int(line.strip('\n')))
	
	return month_dict;
	
	

def mean(monthList):
	if len(monthList) == 0:
		return float('nan')
	
	floatNums = (float(x) for x in monthList)
	return sum(floatNums) / len(monthList)

def three_degrees(month):
	month["maxdev"] = []
	month["mindev"] = []
	for x in month["max"]
		if abs(x - mean) <= 3:
			month["maxdev"].append(x)
	
	for x in month["min"]
		if abs(x - mean) <= 3:
			month["mindev"].append(x)


if __name__ == "__main__":
	main()

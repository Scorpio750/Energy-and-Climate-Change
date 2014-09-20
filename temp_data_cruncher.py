#!/usr/bin/python

import sys

months = {}

def main():

	# loops over input arguments and creates month dicts to be stored in months
	for x in sys.argv:
		if x == "temp_data_cruncher.py":
			continue
		else:
			month_name = x
			months[month_name] = monthCreate(month_name)

	# calculate mean and deviance
	for month in months:
		months[month]["max_mean"] = mean(months[month]["max"])
		months[month]["min_mean"] = mean(months[month]["min"])
		three_degrees(months[month])

	# output shit
	for month in months:
		print months[month]["name"] + "\nMax Mean: " + str(months[month]["max_mean"]) + "\nDeviants: "
		for i in months[month]['maxdev']:
			print i
		print "\nMin Mean: " + str(months[month]["min_mean"]) + "\nDeviants: "
		for i in months[month]['mindev']:
			print i

def monthCreate(month):
	month_dict = {}
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

	return month_dict



def mean(monthList):
	if len(monthList) == 0:
		return float('nan')

	floatNums = (float(x) for x in monthList)
	return sum(floatNums) / len(monthList)

def three_degrees(month):
	month["maxdev"] = []
	month["mindev"] = []
	for x in month["max"]:
		if abs(x - month["max_mean"]) <= 3:
			month["maxdev"].append(x)

	for x in month["min"]:
		if abs(x - month["min_mean"]) <= 3:
			month["mindev"].append(x)


if __name__ == "__main__":
	main()

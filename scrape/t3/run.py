from bs4 import BeautifulSoup
import requests 
import csv 
import argparse

# init argparse
parser = argparse.ArgumentParser(description = "program's argument")
# add argument
parser.add_argument('-o','--out',action = 'store_true',help = 'option to export your scraped data or print it out in the terminal, default is False')
# create argument
args = parser.parse_args()

if __name__ == "__main__":

	if args.out:
		print("Exported data")
	else:
		print("Print out data")
'''
If you choice export it will export scraped data of each page into csv file
The url base on what is your target, the server will give you the response follow your arugment
'''
import csv 
import requests 
import argparse
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# init argparse
parser = argparse.ArgumentParser(description = "program's arguments")
# add argument
parser.add_argument('-o','--out',action = 'store_true',help = 'option to export your scraped data or print it out in the terminal, default is False')
# create argument
args = parser.parse_args()

# what is your keyword
keyword = input('What is your job? ')
keyword = keyword.replace(' ','-')

def scrape_page(soup):
	'''
	Get soup and return scraped data
	Arguments:
		- soup: beautifulsoup object
	Returns:
		collections: (list of list) scraped data
	'''
	pass

if __name__ == "__main__":

	# url
	
	# print(my_url)

	if args.out:
		# init csv file
		# csv_file = open(f'./scrape/t3/s{i}.csv')
		# csv_writer = csv_file.writer(csv_file)
		# csv_writer.writerow(csv_file)
		# # add your collections
		# csv_writer.writerows(collections)
		# #close file
		# csv_file.close()
		print("Data exported!")
	
	else:
		# table = PrettyTable(fields_name = columns)
		# table.add_rows(collections)
		# print(table)
		print("Data printed out!")
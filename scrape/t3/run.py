'''
If you choice export it will export scraped data of each page into csv file
The url base on what is your target, the server will give you the response follow your arugment
'''
import requests 
import csv 
import argparse
from requests_html import HTMLSession
from prettytable import PrettyTable

url = 'https://www.vietnamworks.com/'
# 'salary','benifit','position','requires','description','location'
columns = ['salary','benifit','position','requires','description','location']

# init argparse
parser = argparse.ArgumentParser(description = "program's arguments")
# add argument
parser.add_argument('-o','--out',action = 'store_true',help = 'option to export your scraped data or print it out in the terminal, default is False')
# create argument
args = parser.parse_args()

# what is your keyword
keyword = input('What is your job? ')
keyword = keyword.replace(' ','-')

# get the session from your html session
session = HTMLSession()

def scrape_page(response):
	'''
	Get soup and return scraped data
	Arguments:
		- response: server response
	Returns:
		collections: (list of list) scraped data
	'''
	# col-12 col-lg-9 no-padding-responsive search-result-listJob
	listjob = response.html.find('div.search-result-listJob',first = True)
	jobs = listjob.find('div.paddingMore')
	print(jobs)

if __name__ == "__main__":

	# url
	my_url = url + keyword + '-kv'

	# send request the server
	response = session.get(my_url)
	# print(response.html.html)

	# scrape data
	# init your collections
	collections = []

	# scrape the data from the soup
	scrape_page(response)

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
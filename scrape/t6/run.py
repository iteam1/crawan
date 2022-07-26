'''
if you choice export it will export scraped data of each page into csv file
The url base on what is your target, the server will give you the response follow your arugment
https://careerbuilder.vn use javascript so render your response before scraping
consider about job-argument and page-argument in the same time
if the next page is blank you still can save the previous scraped data
'''
import csv 
import requests 
import argparse
from requests_html import HTML,HTMLSession
#from bs4 import BeautifulSoup
from prettytable import PrettyTable

# init some params
url = 'https://careerbuilder.vn/' # the base url
filename = 't6' # the name for csvfile if you store scraped information into csv file

# inspect and define which information you can scrape from page
# ['title','company','salary','location','benefit','date','detail-link']
columns = ['title','company','salary','location','benefit','date','detail-link']

# init argparse
parser = argparse.ArgumentParser(description = "program's arguments")
# add argument
parser.add_argument('-o','--out',action='store_true',help='option to export your scraped data or print it out in the terminal, default is False')
parser.add_argument('-d','--directory',type=str,help='the directory where you can store data',default='./analyze/data')
parser.add_argument('-f','--filename',type=str,help='csv filename',default =filename)
# create argument
args = parser.parse_args()

def scrape_page(page):
	'''
	Get soup and return scraped data
	Arguments:
		- soup: beautifulsoup object
	Returns:
		collections: (list of list) scraped data
	'''
	# init the collections
	collections = []
	# find the job div
	jobs = page.find('div.job-item ')
	# print(len(jobs))
	for job in jobs:
		title = job.find('a.job_link',first=True).text.strip()
		detail_link = job.find('a.job_link',first=True).attrs['href']
		company = job.find('a.company-name',first=True).text.strip()
		salary = job.find('div.salary',first=True).text.strip()
		location = job.find('div.location',first=True).text.strip()
		# find benefit, sometime it does not have benefit
		try:
			benefit = job.find('ul.welfare',first=True).text.strip().replace('\n','-')
		except Exception as e:
			benefit = None
		#date
		date = job.find('time',first=True).text.strip()
		# append the collections
		collections.append([title,company,salary,location,benefit,date,detail_link])
	return collections

if __name__ == "__main__":

	# what is your keyword
	keyword = input('What is your job? ')
	keyword = keyword.replace(' ','-')
	pages = int(input('How many page you want to scrape? '))

	for i in range(1,pages+1):
		arguments = 'viec-lam/' + keyword + f'-k-trang-{i}-vi.html'
		# your url
		my_url = url + arguments
		# print out and try to open the link with Ctrl+Left-click
		print('URL: ' + my_url)
		
		# send a request and try to catch the response
		# response = requests.get(my_url)
		# soup = BeautifulSoup(response.text,features = 'lxml')
		# print(soup.prettify())
		
		session = HTMLSession()
		response = session.get(my_url)
		# print(response.html.html)
		collections = scrape_page(response.html)

		# option to display
		if args.out:
			# init csv file
			csv_file = open(f'{args.directory}/{args.filename}_{i}.csv','w')
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow(collections)
			# add your collections
			csv_writer.writerows(collections)
			# close file
			csv_file.close()
			print("Data exported!")
		
		else:
			table = PrettyTable(fields_name = columns.remov)
			table.add_rows(collections)
			print(table)
			print("Data printed out!")
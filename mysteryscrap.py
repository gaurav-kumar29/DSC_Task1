import requests
import time
import csv

import selenium
from selenium import webdriver
from bs4 import BeautifulSoup as bs

def scrape(driver, sbd): 
	html = driver.page_source
	soup = bs(html, "html.parser")

	allBooks = soup.find_all('article', class_='product_pod')

	with open("mystery.csv", "a") as dump: 
		writer = csv.writer(dump)

		for book in allBooks: 
			title = book.find('h3').find('a').get('title').replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u201c', '"').replace(u'\u201d', '"').replace(u'\xe1',' ').replace(u'\xe9',' ')
			
			price = "$" + book.find('p', class_='price_color').text.strip().encode('ascii','ignore').decode('ascii')
			ifAvailable = book.find('p', class_='instock').text.strip().encode('ascii','ignore').decode('ascii')
			
			rating = book.find('p', class_='star-rating').get('class')[1]

			writer.writerow([title,rating,price,ifAvailable])
			
			

	driver.find_element_by_link_text('next').click() 






path = '/Users/gauravkumar/Downloads/chromedriver'


url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"


toStop = 2
currentPage = 0


driver = webdriver.Chrome(path)
driver.get(url)


while (currentPage < toStop):
	scrape(driver, url)
	currentPage+=1

time.sleep(3)
driver.quit()


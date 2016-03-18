##########################################################################
#								IDEAS									 #
# 1. Use discrete math to find fastest way to complete a tree 			 #
#	 from parent node. 													 #
#		a. Deploy on the 'sides'(?) of the tree rather than the top		 #
# 2. Shut Down in an orderly manner										 #
# 3. Abandon Tree(Stops crawling a tree and goes to another)			 #
# 4. Energy Saver Mode. Turns off and on at certain times automatically  #
# 5. Or dims screen. 													 #
# 6. Have the visitor-crawlers wait by using WebDriverWait()			 #
##########################################################################
#								GOALS									 #
# 1. Click on sites and visit them										 #
# 2. Removes "None." entries from ListOfLinks							 #
# 3. Removes duplicate and equivalent websites							 #
##########################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import WebDriverException
# from selenium.common.exceptions import NoSuchWindowException
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException

import time

import urllib.request

def init_startup_procedure():
	browser_func = webdriver.Chrome("/Users/rich/Desktop/chromedriver")
	browser_func.get("https://www.bumoodle.com") #Initial Website
	window = browser_func.current_window_handle
	return browser_func, window

def fetch_elements(target_window):
	#Find all <a > and put in elements
	elements = target_window.find_elements_by_xpath("//a")
	return elements

def fetch_attribute(target_elements):
	ListOfLinks_func = []
	#Find attribute href and print
	for attribute in target_elements:
		link = attribute.get_attribute("href")
		#print("This is the link: %s." % link)

		#Add new link to the list of links
		ListOfLinks_func.append(link)
	#print(ListOfLinks_func)
	return ListOfLinks_func

def get_ListOfLinks(target_window):
	elements = fetch_elements(target_window)
	ListOfLinks = fetch_attribute(elements)
	return ListOfLinks

def link_selector(target_window, click_list):
	ListOfLinks_child = []
	# Select link from the list of links
	for link in click_list:
		# Visit
		# Sweep for links
		ListOfLinks_child = page_visitor(browser, link, ListOfLinks_child)
		# Close ALL windows
		target_window.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
		ListOfLinks_child = []
		# Report the recently swept links
		#	Consider where to stash links
		#	Handle efficient visiting paths
		#	Create list memory cap i.e. 2 GB

def page_visitor(target_window, link, ListOfLinks_child):
	target_window.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
	target_window.get(link)
	ListOfLinks_child = get_ListOfLinks(target_window)
	return ListOfLinks_child

if __name__ == "__main__":
	#list for the links found on website
	ListOfLinks = []
	browser, main_window = init_startup_procedure()
	elements  = fetch_elements(browser)
	ListOfLinks = fetch_attribute(elements)

	#print("*************Out****************")
	#print(ListOfLinks)

	visited = link_selector(browser, ListOfLinks)

	browser.quit()












































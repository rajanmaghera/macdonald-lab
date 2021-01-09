from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_binary
import xlsxwriter

gene = "C10orf10"

driver = webdriver.Chrome()
driver.get('https://www.genecards.org/cgi-bin/carddisp.pl?gene='+gene)

driver.get('https://www.genecards.org/cgi-bin/carddisp.pl?gene='+gene)

driver.get('https://www.genecards.org/cgi-bin/carddisp.pl?gene='+gene)
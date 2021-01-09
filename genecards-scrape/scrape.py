from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
import xlsxwriter

gene = "C10orf10"

# open website
driver = webdriver.Chrome()
driver.get('https://www.genecards.org/cgi-bin/carddisp.pl?gene='+gene)
assert "GeneCards" in driver.title

# find gene aliases
titles = driver.find_element(By.ID, 'aliases_descriptions')
columns = titles.find_elements(By.CLASS_NAME, 'col-sm-6')

for column in columns:

    item = column.find_elements(By.TAG_NAME, 'li')
    for title in item:

        title_nums = title.find_elements(By.TAG_NAME, 'a')
        num_strings = ""
        for super in title_nums:
            num_strings += " " + super.text

        real_title = title.text.replace(num_strings, "")

        print(real_title)

# find summaries
summaries = driver.find_element(By.ID, 'summaries')
summaries = summaries.find_elements(By.CLASS_NAME, 'gc-subsection')

for summary in summaries:

    title = summary.find_element(By.TAG_NAME, 'h3')
    print(title.text)

    body = summary.text.replace(title.text, '')
    print(body)

    # a_links = summary.find_elements(By.TAG_NAME, 'a')

    # for link in a_links:
    #     link.get_attribute('href')
    #     if link.text is not "":
    #         body = body.replace(link.text, link.get_attribute('href'))


driver.quit()
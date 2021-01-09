"""
GeneCards Scraper

This script uses selenium to scrape the GeneCards database for information and output its results into a .xlsx file.

Note: Chrome is required on the computer.

Installation:

1. Run the following command to install all dependencies: pip3 install selenium xlsxwriter pandas openpyxl
2. Install the correct version of the Chrome Driver.
    a) Find the Chrome version in Menu > Help > About Google Chrome.
    b) Go to https://pypi.org/project/chromedriver-binary/#history and find the closest version number to your Chrome version.
    c) Copy the install command on the specific version of the chromedriver and install like before.

Usage:

python3 210109_genecards_scrape.py <path to spreadsheet>
"""

import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import xlsxwriter
import pandas as pd
import os

# initalize command line argument parser

parser = argparse.ArgumentParser(description="This script uses selenium to scrape the GeneCards database for information and output its results into a .xlsx file.")
parser.add_argument('path', type=str, help='path to target')
args = parser.parse_args()

# open input sheet

try:
    df = pd.read_excel(args.path, 0)
    genes = df["Gene ID"]
except:
    print("There was an error opening the spreadsheet.")
else:

    row = 0

    # initiate output sheet with formatting

    workbook = xlsxwriter.Workbook(os.path.splitext(args.path)[0] + '_scraped.xlsx')
    worksheet = workbook.add_worksheet('Sheet1')

    cell_format = workbook.add_format()
    bold = workbook.add_format({'bold': True})
    cell_format.set_text_wrap()
    cell_format.set_align("top")

    worksheet.set_column("A:A",30,cell_format)
    worksheet.set_column("B:B",40,cell_format)
    worksheet.set_column("C:C",70,cell_format)

    # open browser

    driver = webdriver.Chrome()

    # start through each gene

    for gene in genes:

        worksheet.write(row, 0, gene)

        # open website

        try:
            
            driver.get('https://www.genecards.org/cgi-bin/carddisp.pl?gene='+gene)
            #assert "GeneCards" in driver.title

            # find gene aliases

            titles = driver.find_element(By.ID, 'aliases_descriptions')
            columns = titles.find_elements(By.CLASS_NAME, 'gc-subsection')

            gene_string = ""

            columns = [columns[0]]

            for column in columns:

                item = column.find_elements(By.TAG_NAME, 'li')
                for title in item:

                    title_nums = title.find_elements(By.TAG_NAME, 'a')
                    num_strings = ""
                    for super in title_nums:
                        num_strings += " " + super.text

                    real_title = title.text.replace(num_strings, "")

                    gene_string += real_title + "\n"

            # write aliases to sheet

            worksheet.write(row, 1, gene_string[0:-1])

            # find summaries

            summaries = driver.find_element(By.ID, 'summaries')
            summaries = summaries.find_elements(By.CLASS_NAME, 'gc-subsection')

            summary_array = []

            for summary in summaries:

                title = summary.find_element(By.TAG_NAME, 'h3')

                if title.text != "":
                    summary_array.append(bold)
                    summary_array.append(title.text)

                body = summary.text.replace(title.text, '')
                
                summary_array.append(body + "\n\n")

            # remove extra new lines

            ind = len(summary_array)-1

            if summary_array[ind] == "\n\n":
                summary_array.pop(ind)
            else:
                summary_array[ind] = summary_array[ind][0:-4]

            # write summary to sheet

            worksheet.write_rich_string(row, 2, *summary_array)
            
            print("Completed: "+ gene + " [" + str(row+1) + "/" + str(len(genes)) + "]")
        
        except:
            
            print("There was an error processing: " + gene)

        # increment row

        row += 1

    # close programs

    driver.quit()
    workbook.close()
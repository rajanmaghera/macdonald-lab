import xlsxwriter
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('scrape.xlsx', 0)

list = df["Gene ID"]
print(list[2])
# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import ssl

# Create an URL object
url = 'https://www.worldometers.info/coronavirus/'
#url = 'https://bi.gks.ru/biportal/contourbi.jsp?allsol=1&solution=Dashboard&project=%2FDashboard%2Ftrade'
# Create object page
page = requests.get(url, verify=False)


# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')
#print(soup)

# Obtain information from tag <table>
table1 = soup.find('table', id='main_table_countries_today')
# Obtain every title of columns with tag <th>
headers = []
print(soup)
#for i in table1.find_all('th'):
#    title = i.text
#    headers.append(title)
# Convert wrapped text in column 13 into one line text
#headers[13] = 'Tests/1M pop'
# Create a dataframe
#mydata = pd.DataFrame(columns = headers)
# Create a for loop to fill mydata
#for j in table1.find_all('tr')[1:]:
#    row_data = j.find_all('td')
#    row = [i.text for i in row_data]
#    length = len(mydata)
#    mydata.loc[length] = row
# Drop and clearing unnecessary rows
#mydata.drop(mydata.index[0:7], inplace=True)
#mydata.drop(mydata.index[222:229], inplace=True)
#mydata.reset_index(inplace=True, drop=True)

# Drop “#” column
#mydata.drop('#', inplace=True, axis=1)
# Export to csv
#mydata.to_csv('covid_data.csv', index=False)

# Try to read csv
#mydata2 = pd.read_csv('covid_data.csv')
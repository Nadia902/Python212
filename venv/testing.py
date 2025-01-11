# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import ssl

# Create an URL object
#url = 'https://www.worldometers.info/coronavirus/'
url = 'https://bi.gks.ru/biportal/contourbi.jsp?project=%2FDashboard%2Ftrade&report=_1102_%D0%98%D0%BD%D0%B4_%D1%84%D0%B8%D0%B7_%D0%BE%D0%B1%D1%8C%D0%B5%D0%BC%D0%B0_-_%D0%92%D0%B8%D1%82%D0%B0&toolbar=off&slice=slice1&view=view1'
# Create object page
page = requests.get(url, verify=False)

# parser-lxml = Change html to Python friendly format
# Obtain page's information
sp2 = []
soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find('div', id='cbi_tree')
for plugin in table1:
     name = plugin.text
     sp2.append(name)
print(sp2)

import requests
from bs4 import BeautifulSoup

s = requests.Session()
grd = '7|0|37|https://bi.gks.ru/biportal/ddb/|E61BE9F1423223C71D44715399A77A8D|com.contourcomponents.ddb.client.DashboardInitService|getResizedImages|com.contourcomponents.ddb.client.DashboardInitData$GetResizeImageInData/3245734004|java.util.ArrayList/4159755760|com.contourcomponents.ddb.client.DashboardInitData$GetGridImageData/2089332423|view1|dashboardlayout1|_1102_Инд_физ_обьема_-_Вита|slice1|com.contourcomponents.ddb.client.DashboardRequest/4155753960|[Z/1413617015|java.lang.Long/4227064769|[I/2970817851|java.util.HashMap/1797211028|java.lang.String/2004016611|period1|[Ljava.lang.Boolean;/2507200464|java.lang.Boolean/476441737|period2|id_trade_type|region.ccube.1|_1102_Инд_физ_обьема_-_Вита/slice1|report11|1|report14|allsol|solution|Dashboard|project|/Dashboard/trade|report|slice|tabindex|0|grid|1|2|3|4|1|5|5|6|0|6|1|7|0|8|9|0|10|6|11|0|590|12|0|0|0|0|13|2|0|0|0|0|0|14|fRhZYJQA|15|2|-1|-1|0|0|0|0|0|16|4|17|18|19|11|20|1|20|1|20|1|20|1|20|1|20|1|20|1|20|1|20|1|20|1|20|0|17|21|19|12|20|1|20|1|20|1|20|1|20|1|20|1|20|0|20|1|20|1|20|1|20|0|-35|17|22|19|3|20|1|20|1|20|0|17|23|19|9|20|1|20|0|20|1|20|1|20|1|20|1|20|1|20|1|20|1|24|0|16|4|-10|-10|-23|-23|-36|-36|-41|-41|0|0|0|96|96|0|0|0|0|0|0|16|4|-10|-11|-23|-24|-36|-37|-41|-42|0|-1|-1|0|0|0|0|0|0|23|0|0|0|25|0|0|1|0|0|26|0|873|27|16|7|17|28|17|26|17|29|17|30|17|31|17|32|17|33|17|10|17|34|17|11|17|35|17|36|17|37|17|8|0|1|0|0|0|A|0|27|0|0|0|0|0|0|0|0|0|57|0|0|0|0|0|819|6|0|'
url = 'https://bi.gks.ru/biportal/contourbi.jsp?allsol=1&solution=Dashboard&project=%2FDashboard%2Ftradehttps://bi.gks.ru/biportal/contourbi.jsp?allsol=1&solution=Dashboard&project=%2FDashboard%2Ftrade'
cookies = {'JSESSIONID': '0C2A62338BE0C10678A87DDED2872EAA', 'https%3A%2F%2Fbi.gks.ru%2Fbiportal%2Fddb%2Ftheme':
    '%7B%22state%22%3A%7B%22id%22%3A%22s%3Agray%22%2C%20%22file%22%3A%22s%3Agxt%2Fcss%2Fgxt-gray.css%22%7D%7D'}
#r = s.get(url,verify=False, cookies=cookies)
headers = {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br, zstd',
          'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
          'connection': 'keep-alive', 'content-length': '1469', 'content-type': 'text/x-gwt-rpc; charset=UTF-8',
          'cookie': 'JSESSIONID=0C2A62338BE0C10678A87DDED2872EAA; https%3A%2F%2Fbi.gks.ru%2Fbiportal%2Fddb%2Ftheme=%7B%22state%22%3A%7B%22id%22%3A%22s%3Agray%22%2C%20%22file%22%3A%22s%3Agxt%2Fcss%2Fgxt-gray.css%22%7D%7D',
          'host': 'bi.gks.ru', 'origin': 'https://bi.gks.ru', 'referer': 'https://bi.gks.ru/biportal/contourbi.jsp?allsol=1&solution=Dashboard&project=%2FDashboard%2Ftrade',
          'sec-ch-ua':'"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-mobile':'?0', 'sec-ch-ua-platform':'"Windows"',
          'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
          'x-gwt-module-base': 'https://bi.gks.ru/biportal/ddb/', 'x-gwt-permutation': '8F48688F2C090087DFADA5B0839EEF3D'}
r = s.post(url,  data=grd.encode('utf-8'), cookies=cookies, headers=headers, verify=False)
with open("ind.html", "w") as file:
    file.write(r.text)
soup = BeautifulSoup(r.text)
print(soup)






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
import time
import os
import re
import openpyxl
import csv


def web_save():
    options = Options()
    options.add_argument("-headless")
    profile = webdriver.FirefoxProfile()
    profile.set_preference("security.enterprise_roots.enabled", True)
    driver = webdriver.Firefox(options=options)
    driver.get("https://bi.gks.ru/biportal/contourbi.jsp?allsol=1&solution=Dashboard&project=%2FDashboard%2Ftrade")
    # делаем задержку выполнения кода, так как сайт является динамическим и код выполняется быстрее,
    # чем прогружаются элементы html
    try:
        time.sleep(3)
        clickable = driver.find_element(By.XPATH, '//*[@id="x-auto-0__x-auto-0_x-auto-18"]/table/tbody/tr/td[2]/img')

    except:
        time.sleep(10)
        clickable = driver.find_element(By.XPATH, '//*[@id="x-auto-0__x-auto-0_x-auto-18"]/table/tbody/tr/td[2]/img')
    clickable.click()
    driver.implicitly_wait(10)
    clickable = driver.find_element(By.XPATH, '//*[@id="x-auto-0__x-auto-0_x-auto-91"]/table/tbody/tr/td[5]/span/span')
    clickable.click()
    clickable = driver.find_element(By.XPATH, '//*[@id="x-auto-100__x-auto-96"]/a[2]/em/span/span')
    clickable.click()
    try:
        clickable = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/table/tbody/tr[2]/td/div/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td/div/div[2]/div[1]/div/div/div[2]/table/tbody/tr[1]/td/div/table/tbody/tr/td[2]/div/span')
    except:
        time.sleep(3)
        clickable = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/table/tbody/tr[2]/td/div/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td/div/div[2]/div[1]/div/div/div[2]/table/tbody/tr[1]/td/div/table/tbody/tr/td[2]/div/span')
    clickable.click()
    clickable = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[11]/div/table/tbody/tr/td[5]/div/em/button/img')
    clickable.click()
    clickable = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div/table/tbody/tr/td[3]/div/a')
    clickable.click()
    driver.close()
    driver.quit()
    csv_save()


def csv_save():
    file_path = None
    directory = 'C:/Users/Admin/Downloads/'
    pattern = re.compile(r'tmp_exp[0-9a-f\-]+_1102 - Инд физ обьема_Таблица_\.xlsx')  #ищем файл по названию с регулярным ввыражением

    for file_name in os.listdir(directory):
        if pattern.match(file_name):
            file_path = os.path.join(directory, file_name)

#    list_of_files = glob.glob('C:/Users/Admin/Downloads/*')   поиск последнего файла с более новой датой
#    latest_file = max(list_of_files, key=os.path.getctime)
    ws = openpyxl.load_workbook(file_path)
    wb = ws.active
    time.sleep(2)
    wb.delete_rows(27, 74)
    wb.delete_cols(2, 42)
    wb.delete_cols(5, 3000)
    # для сохранения по другому пути
    # load_dotenv()
    # новый путь для сохранения
    # PATHS = os.getenv("LD_PRELOAD")
    ws.save('static.xlsx')
    wb = openpyxl.load_workbook('static.xlsx')
    sh = wb.active
    with open('static.csv', 'w', newline="") as f:
        c = csv.writer(f, delimiter=';', lineterminator='\r')
        for r in sh.rows:
            c.writerow([cell.value for cell in r])


web_save()

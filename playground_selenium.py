import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.ynet.co.il")
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

with open("webpage_file1.html", "w") as f:
    f.write(driver.page_source)
with open('webpage_file2.html', 'w') as f:
    html_source_code = driver.execute_script("return document.body.innerHTML;")
    f.write(html_source_code)
    #print(driver.page_source)

input('finished?')
driver.close()
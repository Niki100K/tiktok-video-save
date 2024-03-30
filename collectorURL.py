from selenium import webdriver
from selenium.webdriver.chrome.options import Options


print("Opening Chrome...")
options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)

# Change the link to the TikTok account you want to extract the links from
driver.get("https://www.tiktok.com/@username")


print("\033[31m" + "Enter (finish) When you are ready\n")
while True:
    question = input("\033[32m")
    if question.lower() == 'finish':
        break
    else:
        print("\033[31m" + 'Incorrect')


# This class is subject to change, so make sure you inspect the page and find the correct class
class_name = ""

script  = "let links = [];"
script += "document.getElementsByClassName(\""
script += class_name
script += "\").forEach(item => { links.push(item.querySelector('a').href)});"
script += "return links;"

urls_to_download = driver.execute_script(script)

print("\033[37m" + " Fetch " + "\033[35m" + f"{len(urls_to_download)}" + "\033[37m" + " link to clips")
for url in urls_to_download:
    print(f"\"{url}\",")

driver.quit()

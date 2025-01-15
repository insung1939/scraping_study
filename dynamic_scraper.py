from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
from file import save_to_file

p = sync_playwright().start()
browser = p.chromium.launch(headless = False)

page = browser.new_page()
page.goto("https://www.wanted.co.kr")

time.sleep(5)

page.click("button.Aside_searchButton__rajGo")

time.sleep(5)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(5)

page.keyboard.down("Enter")

time.sleep(5)

page.click("a#search_tab_position")

for _ in range(5):
    time.sleep(5)
    page.keyboard.down("End")

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__REty8")

jobs_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_ = "JobCard_title__HBpZf").text
    company_name = job.find("span", class_ = "JobCard_companyName__N1YrF").text

    job = {
        "title": title,
        "company_name": company_name,
        "link": link,
    }

    jobs_db.append(job)

save_to_file('flutter', jobs_db)
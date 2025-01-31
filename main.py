from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
app = Flask("JObScrapper")
@app.route("/") # decorator
def home():
    return render_template("home.html")

@app.route('/search')
def search():
    keyword = request.args.get('keyword')

    url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find('section', class_='jobs').find_all('li')[1:-1]

    job_db = []

    for job in jobs:
        title = job.find('span', class_='title').text
        company, position, *region = job.find_all('span', class_='company')
        url = job.find('div', class_="tooltip--flag-logo").next_sibling["href"]
        job_data = {
            'title': title,
            'company': company.text,
            'position': position.text,
            'location': "No Location" if not len(region) else region[0].text,
            "link": f"https://weworkremotelly.com{url}"
        }
        if keyword in job_data['title']:
            job_db.append(job_data)
    return render_template("search.html", keyword=keyword, jobs = job_db)

if __name__ == "__main__":
    app.run(port=5001)  # 5001 또는 다른 사용 가능한 포트를 지정
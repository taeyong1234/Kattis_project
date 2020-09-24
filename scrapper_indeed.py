import requests  # html 을 가져오기
from bs4 import BeautifulSoup  # html에서 데이터 가져오기

Limit = 50
url = 'https://www.indeed.com/jobs?q=Python&l=New+York+State&radius=100&limit=50'


def extract_indeedpages():
    resul = requests.get(url)

    soup = BeautifulSoup(resul.text, 'html.parser')

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")  # links

    spans = []
    for link in links[:-1]:
        spans.append(int(link.find('span').string))

    max_page = spans[-1]
    return max_page

'''
def extracting_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]

    company = html.find("span", {"class": "company"})
    if company.find("a") is None:
        company = company.string
    else:
        company = company.find("a").string
    company = company.strip()

    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]

    job_id = html["data-jk"]

    return {"title": title, "company": company, "location": location,
            "job_id": f"https://www.indeed.com/viewjob?jk={job_id}"}


def extract_indeed_jobs(last_page):
    jobs = []

    for page in range(2):
        print(f"Scrapping page {page}")
        result = requests.get(f"{url}&start={page*Limit}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

        for result in results:
            job = extracting_job(result)
            jobs.append(job)

    return jobs


'''

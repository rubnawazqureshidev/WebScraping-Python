import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def scraping():
    page = requests.get("https://www.learninsta.com/ncert-solutions-for-class-6-maths-chapter-1")
    soup = BeautifulSoup(page.content, "lxml")
    title = soup.find('h1', class_='entry-title').text
    content = soup.find('div', class_='entry-content').text

    filename = title + '.json'
    result = {
        "title": title,
        "content": content
    }

    with open(filename, 'w') as outfile:
        json.dump(result, outfile)

    return result


@app.get("/subjects")
def subjects():
    page = requests.get('https://www.learninsta.com/ncert-solutions-for-class-12')
    soup = BeautifulSoup(page.content, "lxml")
    content_area = soup.find('div', class_='entry-content')
    content_area_ul = content_area.find('ul')
    title = soup.find('h1').text
    class_subjects = []
    class_subjects_raw = content_area_ul.find_all('li')

    for subject in class_subjects_raw:
        class_subjects.append(subject.a.text)

    filename = title + '.json'
    pathname = 'subjects/'+filename

    result = {
        "class": title,
        "subjects": class_subjects
    }

    with open(pathname, 'w') as outfile:
        json.dump(result, outfile)

    return result

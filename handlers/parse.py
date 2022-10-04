from pprint import pprint

import requests
from bs4 import BeautifulSoup as BS

URL = "https://www.securitylab.ru/news/"

HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all("a", class_="article-card inline-card")
    articles = []
    for item in items:
        datetime = item.find("time").getText()
        # print(datetime)
        articles.append({
            "link": "https://securitylab.ru" + item.get("href"),
            "title": item.find("h2", class_="article-card-title").getText(),
            "time": datetime[:5],
            "day": datetime[8:].split(", ")[0],
            "year": datetime[8:].split(", ")[1]
        })
    return articles


# html = get_html(URL)
# print(get_d/ata(html.text))


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answers = []
        for i in range(1, 2):
            html = get_html(URL+f"page1_{i}.php")
            current_page = get_data(html.text)
            answers.extend(current_page)
        return answers
    else:
        raise Exception("Error in parser")


if __name__ == '__main__':
    # print(0)
    # print(html.text)
    pprint(parser())
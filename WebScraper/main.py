import json

import requests as req
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

data = []
n = 1

while n <= 50:
    content = req.get(url + f"catalogue/page-{n}.html").content

    soup = BeautifulSoup(content, "html.parser")

    all_books = ".col-xs-6.col-sm-4.col-md-3.col-lg-3"

    books = soup.select(all_books)

    for ind, book in enumerate(books, start=1):
        title = book.h3.a.attrs["title"]
        rating = book.p.attrs["class"][1]
        price = book.select_one(".price_color").string
        image = url + book.img.attrs["src"]

        new_book = {
            "title": title,
            "price": price,
            "rating": rating,
            "image": image,
        }

        data.append(new_book)

    print("Pages: ", n)
    n += 1


with open("books.json", "w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

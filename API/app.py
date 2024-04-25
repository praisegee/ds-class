import requests
from bs4 import BeautifulSoup


res = requests.get(
    "https://stackoverflow.com/questions/18930320/corrupted-vim-indentation"
)

# with open("oic.html", "r") as f:
#     html = f.read()

html = res.text
# print(html)

soup = BeautifulSoup(html, "html.parser")

print(soup.find("h1").text)

# print(soup.prettify())

# print(soup.prettify())
# response = requests.get("https://www.oichub.org/")

# # print(dir(response))
# # print(type(response))

# # print(response.text)

# with open("oic.html", "w") as f:
#     f.write(response.text)

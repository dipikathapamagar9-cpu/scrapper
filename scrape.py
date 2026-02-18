#
import requests
from bs4 import BeautifulSoup 
import json

#url of the websites
url = "http://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        return
    
    #set encoding explicitly to handle special characters correctly
    response.encoding = response.apparent_encoding

    all_books = []
    soup =  BeautifulSoup(response.text,"html.parser")
    books = soup.find_all("article", class_="product_pod")
    for book in books:
    
        title = book.h3.a("title")
        price_text = book.find("p", class_ = "price_color").text
        currency = price_text[0]
        price =float(price_text[1:])
        all_books.append(
            {
                "title":title,
            "price":price,
            "currency":currency,
            }
        )

    return all_books

books = scrape_books(url)
with open("books.json","w",encoding="utf-8") as f:
     

     json.dump(books,f, indent=2,ensure_ascii =False)

     with open("books.csv","w", encoding="utf-8") as f:
         

         json.dump(books,f,indent=2, ensure_ascii=False)

         with open("books.csv","w")as f:
             import csv

             writer = csv.Dictwriter(f, fieldnames = ["title","price","currency"])
             writer.writeheader()
             writer.writerows(books)
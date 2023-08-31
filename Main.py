import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver


userInput = input("URL (eg: google.com): ")
pageUrl = "https://www." + userInput
pageFileName = userInput + ".html"

page = requests.get(pageUrl)
pageLinks = page.links
pageEncoding = page.encoding
pageContent = page.content.decode(pageEncoding)


pageInfoList = [pageUrl, page, pageEncoding, pageContent]
os.system("cls")

pageHTML = open(pageFileName, "w")
for line in pageContent:
    pageHTML.write(line)


for i in pageInfoList:
    if i == pageContent:
        print(f"page html logged in {pageFileName}")
    else:
        print(i)
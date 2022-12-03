# ece464_ps3
The program webscrapes the sandbox bookstore website for title, price, upc, availability, and URL. The data will be stored to a NoSQL database, mongoDB.

To run webscraper:
cd ece464_hw3
scrapy crawl Books

In a separate file, the following queries are included:
1. Find the document that contain the given title
2. Find the title and url using the keyword contained in the title
3. Find the books whose price are lower than £20
4. Find the number of books whose price are lower than £20
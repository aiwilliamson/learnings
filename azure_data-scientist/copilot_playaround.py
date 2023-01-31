# get a list of books from goodreads
# using an api call
# and store them in a csv file

import requests
import csv
import time

def get_books():
    # get a list of books from goodreads
    # using an api call
    # and store them in a csv file
    url = 'https://www.goodreads.com/list/show/1.Best_Books_Ever.json'
    

    

def convert_to_csv(response_text):
    # convert the books to a csv file
    # and save it to a file
    with open('books.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'author', 'rating'])
        i = 0
        for line in response_text.splitlines():
            writer.writerow(line)
            i += 1
            if i == 10:
                break


def get_books_from_csv():
    # get a list of books from a csv file
    with open('books.csv', 'r') as f:
        reader = csv.reader(f)
        books = list(reader)
    return books

if __name__ == '__main__':
    # get the books
    response_text = get_books()
    # convert the books to a csv file
    convert_to_csv(response_text)
    # get the books from the csv file
    books = get_books_from_csv()
    # print the books
    for book in books:
        print(book)
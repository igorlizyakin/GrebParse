import requests
from lxml import etree
import lxml.html
import csv

def parse(url):
    api = request.get(url)
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//ссылка сайта')
    text_translate = tree.xpath('//ссылка сайта')
    with open('text.csv', 'w', newline= '') as csv_file:
        write = csv.writer(csv_file)
        for i in range(len(text_original))
            write.writerow(len(text_original[i]))
            write.writerow(len(text_translate[i]))

def main():
    parse( ' https:')

if __name__ == '__main__':
    main()
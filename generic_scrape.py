#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import csv
import json

# Load csv example
def load_csv():
    list_it = []
    with open('example.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list_it.append({'col1': row['col1'], 'col2': row['col2']})
    return list_it

# Generic scraping example
def scrape_cource():
    cell_list = []
    fail_list = []
    try:
        url = 'http://examplepagetoscrape.com'
        usock = urllib2.urlopen(url)
        html_data = usock.read()
        usock.close()
        # print html_data
        soup = BeautifulSoup(html_data)
        # Find the div that all of the articles live in for the given url
        table_cell = soup.find_all('td');
        for tc in table_cell:
            cell_list.append(tc.string.strip())

    except:
        fail_list.append(pg_num)

    # dump_to_json(cell_list)

# Export to json example
def dump_to_json(data_dict):
    with open('data.json', 'w') as outfile:
        json.dump(data_dict, outfile)

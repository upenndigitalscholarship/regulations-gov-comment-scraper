import requests
import csv
import time
import sys

api_key = '' # insert your api key between quotes
docket_id = '' # insert the docket id between quotes (e.g. VA-2016-VHA-0011)
total_docs = 217568  # total number of documents, as indicated by the page for the given docket id
docs_per_page = 1000  # maximum number of results per page; no reason to change
err_file = None  # a file containing the urls with reported errors; leave this as None most of the time

url = ('https://api.data.gov:443/regulations/v3/'
       'documents.json?api_key={}&dktid={}&rpp={}&po={}')

def make_urls():
    return [url.format(api_key, docket_id, docs_per_page, i)
            for i in range(0, total_docs, docs_per_page)]

def get(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json().get('documents', {})
    else:
        return {}

def save_batch(batch, ix):
    keys = set(k for d in batch for k in d.keys())
    with open('batch_{:03d}.csv'.format(ix), 'w', encoding='utf-8') as op:
        wr = csv.DictWriter(op, fieldnames=sorted(keys))
        wr.writeheader()
        wr.writerows(batch)

def fetch_urls(urls):
    data = {}
    errors = []
    urls = make_urls()
    for i, url in enumerate(urls):
        d = get(url)
        if d:
            data[url] = d
            save_batch(d, i)
        else:
            errors.append(url)
            print('error on url {}'.format(url))
        time.sleep(5)

    with open('error-urls.txt', 'w', encoding='utf-8') as op:
        for e in errors:
            op.write(e)
            op.write('\n')

def fix_errors(err_file):
    with open(err_file, encoding='utf-8') as ip:
        urls = ip.readlines()
    fetch_urls(urls)

def main():
    urls = make_urls()
    fetch_urls(urls)

if __name__ == '__main__':
    if err_file is not None:
        fix_errors(err_file)
    else:
        main()

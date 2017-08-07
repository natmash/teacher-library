from lib import googlebooks
import json as json

def __get_response__(response):
    books = json.loads(json.dumps(response))
    all = []
    if 'items' in books:
        for book in books['items']:
            d = book['volumeInfo']
            r = {}
            r['title'] = d['title']

            if 'authors' in d:
                r['author'] = d['authors']
            else :
                continue

            #figure out 13 vs 10
            if 'industryIdentifiers' in d:
                r['isbn'] = d['industryIdentifiers'][0]['identifier']
            else :
                continue

            if 'imageLinks' in d:
                if 'thumbnail' in d['imageLinks']:
                    r['cover'] = d['imageLinks']['thumbnail']
            else :
                continue

            if 'description' in d:
               r['description'] = d['description']
            else :
                continue

            if 'pageCount' in d:
                r['pages'] = d['pageCount']
            else :
                continue

            all.append(r)
    return all

def author_lookup(author):
    api = googlebooks.Api()
    return __get_response__(api.list('inauthor:' + author,maxResults=40))

def title_lookup(title):
    api = googlebooks.Api()
    return __get_response__(api.list('intitle:' + title, maxResults=40))

def isbn_lookup(isbn):
    api = googlebooks.Api()
    return __get_response__(api.list('isbn:' + isbn))
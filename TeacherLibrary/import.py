import booklookup as b
import sys
from TeacherLibrary.models import Book
from urllib import request


f = open('isbn.txt', 'r')

lines = f.readlines()

for line in lines :
    try :
       line = line.rstrip()
       bk = b.isbn_lookup(line)
       if len(bk) > 0:
           book = Book()
           book.title = bk[0]['title']
           book.author = ', '.join(bk[0]['author'])
           book.isbn = line
           request.urlretrieve(bk[0]['cover'], line + '.jpg')
           book.cover = line + '.jpg'
           book.description = bk[0]['description']
           book.pages = bk[0]['pages']
           book.save()
       else :
           print("Didn't find book for " + line + "...")
    except:
        print('Failed ' + line + ' because of ' +  sys.exc_info()[0])

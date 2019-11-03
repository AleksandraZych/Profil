import csv
from compare import extract_boxoffice, count_awards



def high():
    maxrun=0
    title=''
    maxbox=0
    maxawards=0
    titlea=''
    oscars=0
    o=0
    imdb=0
    maximdb=0
    imbdtitle=''
    titleOscar=''
    with open('Backend_movies.csv','r',encoding ='UTF-8', newline='')as f:
        movie=csv.DictReader(f, delimiter=',')
        for p in movie:
            if any(i.isdigit() for i in p['runtime'])==True:
                runtime=(int(p['runtime'].replace(',','').replace(' min','')))
            if runtime>maxrun:
                maxrun=runtime
                title=p['title']
            k= extract_boxoffice(p['title']) 
            if k>maxbox:
                maxbox=k
                titlebox=p['title']
            a=count_awards(p['title'])
            if a>maxawards:
                maxawards=a
                titlea=p['title']
            iterable = p['awards'].split()
            if 'Won' in iterable:
                o=int(iterable[1])
            if o> oscars:
                oscars=o
                titleOscar=p['title']
            if any(i.isdigit() for i in p['imdb_rating'])==True:
                imdb=float(p['imdb_rating'])
            if imdb>maximdb:
                maximdb=imdb
                imbdtitle=p['title']
        
        print('Runtime', title, maxrun, 'min')
        print('Box Office', titlebox, maxbox ,'$')        
        print('Awards Won', titlea, maxawards )        
        print('Oscars Won', titleOscar, oscars )     
        print('Highest IMDB Rating', imbdtitle, maximdb )             
        

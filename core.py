import csv

    
def write_to_csv(list,mode):
    fieldnames = ['id', 'title', 'year', 'runtime', 'genre', 'director', 'cast', 'writer', 'language', 'country', 'awards', 'imdb_rating', 'imdb_voutes', 'box_office']
    with open('Backend_movies.csv', mode, encoding='utf-8' ) as nn:
        csvwriter = csv.DictWriter(nn, fieldnames=fieldnames)
        csvwriter.writeheader()
        for r in list:
            csvwriter.writerow(r)
            print(r)
def count_awards(title):
    wins=0
    with open('Backend_movies.csv','r',encoding ='UTF-8', newline='')as f:
            movie=csv.DictReader(f, delimiter=',')
            for p in movie: 
                if title in p['title']:
                    iterable = p['awards'].split()
                    if len(iterable)<4 or 'wins' not in iterable: 
                        continue
                    elif 'Won' in iterable:
                        wins=int(iterable[len(iterable)-5])+int(iterable[1])
                    elif 'Nominated' in iterable:
                        wins=int(iterable[len(iterable)-5]) 
                    else:
                        wins=int(iterable[len(iterable)-5])
                    
    return wins
    
    
def count_nominations(title):    #comment not sure about: are wins also nominations?
    nominations=0
    with open('Backend_movies.csv','r',encoding ='UTF-8', newline='')as f:
        movie=csv.DictReader(f, delimiter=',')
        for p in movie: 
            if title in p['title']:
                iterable = p['awards'].split()
                if len(iterable)<4 or 'wins' not in iterable: 
                    continue
                elif 'Won' in iterable:
                    nominations=int(iterable[len(iterable)-2])
                elif 'Nominated' in iterable:
                    nominations=int(iterable[len(iterable)-2])+int(iterable[2])
                else:
                    nominations=int(iterable[len(iterable)-2])
    return nominations
    
    
def extract_boxoffice(title):
    earned=0
    with open('Backend_movies.csv','r',encoding ='UTF-8', newline='')as f:
                movie=csv.DictReader(f, delimiter=',')
                for p in movie:
                    if title in p['title']:
                        if any(i.isdigit() for i in p['box_office'])==True:
                            earned = int((p['box_office'].replace('$', '')).replace(',',''))
    return earned                    
 
#sort and filter 
import csv 
from core import count_awards, count_nominations

def sort_by(arg, TorF):
    reader = csv.DictReader(open('Backend_movies.csv','r',encoding ='UTF-8', newline=''))
    sortedlist = sorted(reader, key=lambda row:( row[arg]), reverse=TorF)
    for s in sortedlist:
        print(s['title'], s[arg])


def sort_by_runtime(TorF):
    with open('Backend_movies.csv','r',encoding ='UTF-8', newline='')as f:
                movie=list(csv.DictReader(f, delimiter=','))
                for p in movie: 
                    if any(i.isdigit() for i in p['runtime'])==True:
                        p['runtime']=(int(p['runtime'].replace(',','').replace(' min','')))
                    else:
                        p['runtime']=0
                sortedlist = sorted(movie, key=lambda row:( row['runtime']), reverse=TorF)
                for s in sortedlist:
                    print(s['title'], s['runtime'])

def sort_by_boxoffice(TorF):
    with open('Backend_movies.csv','r',encoding ='UTF-8', newline='')as f:
                movie=list(csv.DictReader(f, delimiter=','))
                for p in movie: 
                    if any(i.isdigit() for i in p['box_office'])==True:
                        p['box_office'] = int((p['box_office'].replace('$', '')).replace(',',''))
                    else:
                        p['box_office']=0
                sortedlist = sorted(movie, key=lambda row:( row['box_office']), reverse=TorF)
                for s in sortedlist:
                    print(s['title'], s['box_office'])



def filter_by(arg, param):
    with open('Backend_movies.csv','r',encoding ='UTF-8', newline='')as f:
        movie=csv.DictReader(f, delimiter=',')
        if param != 'Won': 
            for p in movie: 
                if param in (p[arg]):  #Director Actor
                    print(p['title'], '-', p)
        else:
            for p in movie: 
                if param not in (p[arg]) and "Nominated" in (p[arg]):
                    print(p)          
                    
                    
def filter_by_boxoffice():
    with open('Backend_movies.csv','r',encoding ='UTF-8', newline='')as f:
                movie=csv.DictReader(f, delimiter=',')
                for p in movie: 
                    if any(i.isdigit() for i in p['box_office'])==True:
                        earned = int((p['box_office'].replace('$', '')).replace(',',''))
                        if earned > 100000000: print(p)
                  

def filter_by_70():    #comment not sure about: are wins also nominations?
        wins=0
        nominations=0
        with open('Backend_movies.csv','r',encoding ='UTF-8', newline='')as f:
            movie=csv.DictReader(f, delimiter=',')
            score= lambda n,w : w/(n+w)*100
            for p in movie: 
                wins=count_awards(p['title'])
                nominations=count_nominations(p['title'])
                
                if nominations!=0 and score(nominations,wins)>70:
                    print(p, '\n Wins:',  wins,'  Nominations:', nominations,'  Won', ("%2.f"%score(nominations,wins)), '% of nominations \n' )
 
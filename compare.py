import csv
from core import count_awards, extract_boxoffice

def compare_runtime(arg, title1, title2):

    with open('Backend_movies.csv','r',encoding ='UTF-8', newline='')as f:
        movie=csv.DictReader(f, delimiter=',')
        for p in movie:
            if title1 in p['title'] and arg=='runtime'and any(i.isdigit() for i in p['runtime'])==True:
                t1_value=(int(p[arg].replace(',','').replace(' min','')))
            if title2 in p['title'] and arg=='runtime'and any(i.isdigit() for i in p['runtime'])==True:
                t2_value=(int(p[arg].replace(',','').replace(' min','')))
        print(t1_value, t2_value)
        if t1_value>t2_value: print("Comparing:", title1, "and", title2, "in", arg, "Winner:", title1) 
        else: print("Comparing:", title1, "and", title2, "in", arg, "Winner:", title2) 



def compare_awards_num(title1, title2):
    val1=count_awards(title1)
    val2=count_awards(title2)
    print(title1, val1, "wins vs.", title2, val2, "wins\n")

   
    
def compare_box(title1,title2):
    val1=extract_boxoffice(title1)
    val2=extract_boxoffice(title2)
    print (title1, val1,'$','\n' ,title2, val2,'$')

def compare_imdb(title1, title2):
    titles=[title1, title2]
    for i in titles:
        with open('Backend_movies.csv','r',encoding ='UTF-8', newline='')as f:
                    movie=csv.DictReader(f, delimiter=',')
                    for p in movie:
                        if i in p['title']:
                            titles.append(p['imdb_rating'])
    print(titles[0],titles[2],'\n',titles[1],titles[3])
       




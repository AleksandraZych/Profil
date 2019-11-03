import csv 
import json
from filling_csv import fill_csv, get_from_api
from core import write_to_csv

#zadziała tylko na oryginalnym pliku - nie moze byc wypełniony już danymi



def complete_data():
    lista_filow=[]
    result=[]
    with open('Backend_movies.csv','r',encoding ='UTF-8', newline='')as f:
        movie=csv.DictReader(f, delimiter=',')
        for row in movie:
            dict1={'id': row['id'], 'title': row['title'], 'year': '', 'runtime': '', 'genre': '', 'director': '', 'cast': '', 'writer': '', 'language': '', 'country': '', 'awards': '', 'imdb_rating': '', 'imdb_voutes': '', 'box_office': ''}
            lista_filow.append(dict(dict1))

    for i in range(len(lista_filow)):
        title_to_fill = lista_filow[i]['title']
        api_all_info = (get_from_api(title_to_fill))
        result.append(fill_csv(lista_filow[i],api_all_info))   
    f.close()

    write_to_csv(result,'w')
    

 
    
    
   
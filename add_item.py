import csv, json, requests
from core import write_to_csv   #(list)
from filling_csv import get_from_api, fill_csv  #(title)

def add_film(title,year):
    result=[]
    with open('Backend_movies.csv','r',encoding ='UTF-8', newline='')as f:
        movie=csv.DictReader(f, delimiter=',')
        for row in movie:
            id=row['id']
        id=int(id)+1
        dict1={'id': id, 'title': title, 'year': year, 'runtime': '', 'genre': '', 'director': '', 'cast': '', 'writer': '', 'language': '', 'country': '', 'awards': '', 'imdb_rating': '', 'imdb_voutes': '', 'box_office': ''}
        
        response = requests.get(("http://www.omdbapi.com/?i=tt3896198&apikey=9ab198b2&"), params={'t': title, 'y':year},)
       
        result.append(fill_csv(dict1,response.json()))   
        f.close()

        write_to_csv(result, 'a')

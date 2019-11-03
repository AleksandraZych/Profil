import csv 
import json
import requests

def get_from_api(title):
    response = requests.get(("http://www.omdbapi.com/?i=tt3896198&apikey=9ab198b2&"), params={'t': title},)
    response.encoding = 'UTF-8'
    return response.json()

def fill_csv(dictCSV, dictAPI):
    dictCSV['year']=dictAPI.get('Year')
    dictCSV['runtime']=dictAPI.get('Runtime')
    dictCSV['genre']=dictAPI.get('Genre')
    dictCSV['director']=dictAPI.get('Director')
    dictCSV['writer']=dictAPI.get('Writer')
    dictCSV['language']=dictAPI.get('Language')
    dictCSV['country']=dictAPI.get('Country')
    dictCSV['awards']=dictAPI.get('Awards')
    dictCSV['imdb_rating']=str(dictAPI.get('imdbRating'))
    dictCSV['imdb_voutes']=str(dictAPI.get('imdbVotes'))
    dictCSV['box_office']=dictAPI.get('BoxOffice')
    dictCSV['cast']=dictAPI.get('Actors')
    return dictCSV
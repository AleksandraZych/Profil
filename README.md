# Profil
Initiation :
While having an Backend_movies.csv downloaded from https://git.profil-software.com/tasks/recruitment-2019-october/tree/master/Backend in folder move to that folder on Command Prompt. 
Then run command: python final_function.py complete data
Now Backend_movies.csv is filled with data from  http://www.omdbapi.com

Sorting :
python final_function.py sort id
You can sort by: 
title,year,runtime,genre,director,cast,writer,language,country,awards,imdb_rating,imdb_voutes,box_office

Filtering: 
Director  -  python core.py filter director "John Carpenter"
Actor  -  python core.py filter actor "John Carpenter"
Movies that was nominated  for Oscar but did not win any.  -  python core.py filter Oscars 
Movies that won more than 80% of nominations  -  python core.py filter nominations (There was no movis with rating over 80%, so I decrease that value to 70%)
Movies that earned more than 100,000,000 $  -  python core.py filter hundred_milion
Only movies in certain Language  -   python final_function.py filter language Spanish

Compare:

IMDb Rating   -  python final_function.py compare_imdb "title 1" "title 2"
Box office earnings  -  python final_function.py compare_boxoffice "title 1" "title 2"
Number of awards won   -  python final_function.py compare_awards "title 1" "title 2" 
Runtime  -  python final_function.py compare_runtime "title 1" "title 2"

Adding movies to data source:

python final_function.py add_film "See" 2019 (Year is optional value)

Showing current highscores :

python final_function.py high score

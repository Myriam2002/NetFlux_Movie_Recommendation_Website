# for quick testing 
import requests
import json
import mysql.connector
# from fuzzywuzzy import fuzz 
# from fuzzywuzzy import process
# import time

connection = mysql.connector.connect(user="SWE", password="123456789000", host="localhost", database="netflux")

cursor = connection.cursor()
# cursor.execute("SELECT title FROM movies")

# similar=process.extract("space",choices=list(map(lambda movies: movies[0],cursor.fetchall())),limit=None)
# similar.sort(reverse = True, key = lambda t: t[1])

# movies=[movie[0] for movie in similar]
# print(movies[0:10])

# cursor.execute("SELECT movieid FROM movies order by release_date desc limit 5")
# result=cursor.fetchall()
# ids=movies = [i[0] for i in result]
# print(ids)
# for i in range(0,len(ids)):
    
#     getResponse = requests.get(f'https://api.themoviedb.org/3/movie/{ids[i]}?api_key=c0bda0be71f7815fd6ba2eb5f5c86fd8')# every movie has a unique ID 
#     getData = getResponse.json() # we request the data from the API and convert it to json
#     getPath = "http://image.tmdb.org/t/p/w500" + getData['poster_path']
#     ids[i]=getPath

# print(ids)   



cursor.execute("select count(movieid) from watched where userid=%s",('Nohaa',))

result=cursor.fetchone() 

print(result[0])


from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import requests
import mysql.connector
from tmdbv3api import TMDb
from tmdbv3api import Movie
import traceback

# https://bootsnipp.com/snippets/Qoe8X--> Css image hover link
app = Flask(__name__)
mysql_username = 'root'
mysql_password = ''
mysql_host = '127.0.0.1'
mysql_port = '3306'
mysql_db = 'flask-test'
mysql_tablename = 'imdb'

# mysql = MySQL(app)
mydb = mysql.connector.connect(
    host=mysql_host,
    user=mysql_username,
    password=mysql_password,
    database=mysql_db
)
cursor = mydb.cursor(buffered=True)


@app.route('/')
def home():

    return render_template('index.html')

# @app.route('/add_movies')
# def add_movies():

#     return render_template('add_movies.html')


@app.route('/search_movies', methods=['POST'])
def search_movies():
    if request.method == 'POST':
        api_key = '5fcb0aa099a1ba810aa4837005668050'
        searchIndex = request.form['searchIndex']
        tmdbobj = TMDb()
        # Set your unique API key, which you'll receive when registering with TMDB;
        TMDb.api_key = api_key
        # Set Language to en, Optional
        tmdbobj.language = 'en'
        # Set debug to True to make it enable for debugging.
        tmdbobj.debug = True
        # Initialize the Movie object and store it in another variable
        movieobj = Movie()
        search = movieobj.search(searchIndex)
        results = []
        for res in search:

            res_dict = {}
            res_dict['id'] = res.id
            res_dict['title'] = res.title
            res_dict['overview'] = res.overview
            if type(res.poster_path) == str:
                res_dict['poster_path'] = f"https://image.tmdb.org/t/p/original{res.poster_path}"
            else:
                res_dict['poster_path'] = "https://leiferproperties.com/wp-content/uploads/NO-IMAGE-AVAILABLE.jpg"
                print(res_dict['poster_path'])
            response = requests.get(
                f'https://api.themoviedb.org/3/movie/{res.id}?api_key={api_key}')
            api_result = response.json()
            res_dict['imdb_id'] = api_result.get('imdb_id')
            results.append(res_dict)
        return render_template('search_movies.html', form_data=results)


@app.route('/add_movies/<imdb_id>', methods=['GET', 'POST'])
def mov_info(imdb_id):
    query=f"Select * from imdb WHERE ib_imdbid='{imdb_id}';"
    cursor.execute(query)
    mov_info = {}
    if(cursor.rowcount==1):
        records=cursor.fetchall()
        records=list(records[0])
        mov_info['title'] = records[2]
        mov_info['plot'] = records[3]
        mov_info['rel_date'] = records[4]
        mov_info['run_time'] = records[5]
        mov_info['directors'] = records[6]
        mov_info['writers'] = records[7]
        mov_info['stars'] = records[8]
        mov_info['genres'] = records[9]
        mov_info['poster'] = records[10]
        mov_info['trailer'] = records[11]
    else:
        cursor.reset()
        response = requests.get(
            f'https://imdb-api.com/en/API/Title/k_l98p8ipa/{imdb_id}')
        result = response.json()  
        mov_info['title'] = result.get('title')
        mov_info['plot'] = result.get('plot')
        mov_info['rel_date'] = result.get('releaseDate')
        mov_info['run_time'] = result.get('runtimeStr')
        mov_info['directors'] = result.get('directors')
        mov_info['writers'] = result.get('writers')
        mov_info['stars'] = result.get('stars')
        mov_info['genres'] = result.get('genres')
        mov_info['poster'] = result.get('image')
        response = requests.get(
            f'https://imdb-api.com/en/API/Trailer/k_l98p8ipa/{imdb_id}')
        result = response.json()
        mov_info['trailer'] = result.get('linkEmbed')
        query = f'''INSERT INTO imdb (ib_imdbid,ib_moviename,ib_plot,ib_reldate,ib_runtime,ib_directors,
        ib_writers,ib_stars,ib_genres,ib_poster,ib_trailer) 
        VALUES (
            "{imdb_id}",
            "{mov_info['title']}",
            "{mov_info['plot']}",
            "{mov_info['rel_date']}",
            "{mov_info['run_time']}",
            "{mov_info['directors']}",
            "{mov_info['writers']}",
            "{mov_info['stars']}",
            "{mov_info['genres']}",
            "{mov_info['poster']}",
            "{mov_info['trailer']}")'''
        try:
            cursor.execute(query)
            mydb.commit()
        except:
            mydb.rollback()
            traceback.print_exc()
    return render_template('add_movies.html', result=mov_info)

@app.route('/movie_list')
def movie_list():
    query="Select * from imdb;"
    cursor.execute(query)
    records=cursor.fetchall()
    records=list(records)
    results = []
    for res in records:
        res_dict = {}
        res_dict['id'] = res[1]
        res_dict['title'] = res[2]
        res_dict['poster_path'] = res[10]
        results.append(res_dict)
        
    return render_template('movie_list.html', form_data=results)
    

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, send_from_directory
import random
import psycopg2
from psycopg2.extras import RealDictCursor
import json
import requests

import logging

logger = logging.getLogger(__name__)



app = Flask(__name__)


app = Flask(__name__, static_folder='static')


# List of movie names from the 1980s
movies_1980s = [
    "The Empire Strikes Back",
    "Raiders of the Lost Ark",
    "E.T. the Extra-Terrestrial",
    "Back to the Future",
    "The Shining",
    "Blade Runner",
    "Ghostbusters",
    "Ferris Bueller's Day Off",
    "The Breakfast Club",
    "The Terminator"
]



def get_db_connection():
    conn = psycopg2.connect(
        dbname='movies_db',
        user='user',
        password='password',
        host='db',
        port='5432'
    )
    return conn

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/movies/test',methods=['GET'])
def get_test():
    return 'passed'

@app.route('/movies/all', methods=['GET'])
def get_movies_all():
    return jsonify(movies_1980s)

@app.route('/movies/ratings', methods=['GET'])
def get_movie_ratings():
    movies_ratings = [{"movie": movie, "rating": random.randint(1, 5)} for movie in movies_1980s]
    return jsonify(movies_ratings)

@app.route('/movies/categories', methods=['GET'])
def get_movie_categories():
    # The URL to which you're posting data
    target_url = 'https://kxacqwm9lc.execute-api.us-west-1.amazonaws.com/ddah_serverless_workshop/movies'
    
    # Dictionary to hold the final results
    final_results = {}

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM movie_categories;')
    movie_categories = cur.fetchall()
    cur.execute('SELECT CATEGORY, RATING FROM movie_categories;')
    genres=cur.fetchall()
    cur.close()
    conn.close()

    
 # Dictionary to hold the final results
    final_results = {}

 # Headers specifying content type
    headers = {
        "Content-Type": "application/json"
    }


    for category in movie_categories:
        
        post_data = {'genre': category['category']}
        # Convert data to JSON format
        payload = json.dumps(post_data)

        response = requests.post(target_url, data=payload, headers=headers)
        
        if response.status_code == 200:
            # Assuming you want to store the JSON response directly
            
            logger.info(response.text)
            result = response.json()
            final_results[category['category']] = category['rating']
        else:
            # Handle error or non-200 responses if needed
            logger.info(response.text)
            final_results[category['category']] = 'Error or non-200 response received'
    return jsonify(genres)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


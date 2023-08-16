from flask import Flask, render_template
import psycopg2
from config import DATABASE_SETTINGS

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(**DATABASE_SETTINGS)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flats")
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)

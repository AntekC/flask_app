from flask import Flask, escape, request, g, jsonify
import sqlite3, json
from flask_cors import CORS
import json 

DATABASE = "./site/database.db"
app = Flask(__name__)
CORS(app)

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = make_dicts
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return 'Index Page'

@app.route('/students/<student_id>/exams', methods=['GET','POST'])
def exams(student_id):
    if request.method == 'POST':
        return f'Dodano egzamin dla studenta {escape(student_id)}'
    else:
        return f'Lista egzaminow studenta {escape(student_id)}'

@app.route('/students/<student_id>/exams/<exam_id>', methods=['GET','PUT','DELETE'])
def student_exams(student_id,exam_id):
    if request.method == 'PUT':
        return f'Aktualizacja egzaminu o id {escape(exam_id)} dla studenta {escape(student_id)}'
    if request.method == 'DELETE':
        return f'Usunieto egzamin o id {escape(exam_id)} dla studenta {escape(student_id)}'
    else:
        return f'Egzamin o id {escape(exam_id)} dla studenta {escape(student_id)}'


@app.route('/students/<student_id>', methods=['GET','PUT','DELETE'])
def student(student_id):
    if request.method == 'PUT':
        return f'Aktualizacja studenta {escape(student_id)}'
    if request.method == 'DELETE':
        return f'Usunieto studenta {escape(student_id)}'
    else:
        return f'{escape(student_id)} profile'


@app.route('/students', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        cur = get_db().cursor()
        cur.execute(f"INSERT INTO students (FirstName, LastName) VALUES ('{request.args['firstname']}','{request.args['lastname']}')")
        get_db().commit()
        get_db().close()
        return f"Dodano studenta {request.args['firstname']} , {request.args['lastname']}"
    else:
        #cur = get_db().execute(query, args)
        #cur.execute('SELECT * FROM students')
        return jsonify(query_db('select * from students'))
        get_db().close()

@app.route('/exams/<exam_id>/students/<student_id>', methods=['GET','PUT','DELETE'])
def exam_id_student_id(student_id,exam_id):
    if request.method == 'PUT':
        return f'Aktualizacja egzaminu o id {escape(exam_id)} dla studenta {escape(student_id)}'
    if request.method == 'DELETE':
        return f'Usunieto egzamin o id {escape(exam_id)} dla studenta {escape(student_id)}'
    else:
        return f'Egzamin o id {escape(exam_id)} dla studenta {escape(student_id)}'

@app.route('/exams/<exam_id>/students', methods=['GET','POST'])
def exams_id_students(exam_id):
    if request.method == 'POST':
        return f'Dodano studentow do egzaminu {escape(exam_id)}'
    else:
        return f'Lista studentow dla egzaminu {escape(exam_id)}'

@app.route('/exams/<exam_id>', methods=['GET','PUT','DELETE'])
def exams_id(exam_id):
    if request.method == 'PUT':
        return f'Aktualizacja egzaminu {escape(exam_id)}'
    if request.method == 'DELETE':
        return f'Usunieto egzamin {escape(exam_id)}'
    else:
        return f'{escape(exam_id)} info'


@app.route('/exams', methods=['GET', 'POST'])
def exam_post():
    if request.method == 'POST':
        return 'Dodano egzamin'
    else:
        return 'Lista egzaminow'

if __name__ == '__main__':
    app.run()

from flask import Flask, escape, request

app = Flask(__name__)

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
        return 'Dodano studenta'
    else:
        return 'Lista studentow'


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


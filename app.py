# Создание простого Hello World на Flask


from flask import Flask, render_template, request

# Создаем объект для Flask app

app = Flask(__name__)

# Временная база
questions = {}


# Создаем первый url

@app.route('/', methods=['GET', 'POST'])
def index():
    # получаем данныe из переменных из frontend
    front_data = request.args.get('search')
    # front_data = request.form.get('search')
    print(front_data)
    test_users = ['Test', 'Test1', 'Test2']
    return render_template('index.html', users=test_users, questions=questions)


# Роут для оброботки вопросов

@app.route('/add-question', methods=['POST'])
def question():
    global questions

    front_question = request.form.get('question')
    front_main_text = request.form.get('main_text')

    questions[front_question] = {"question": front_question,
                                 "main_text": front_main_text,
                                 "answer": []}

    print(front_question, front_main_text)

    return render_template('question.html', exact_question=questions[front_question])


# Динамическая ссылка - /ip/какаята ссылка

@app.route('/<string:some_url>')
def some_dynamic(some_url):
    return str(some_url)


# Запуск
app.run()

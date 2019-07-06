from flask import Flask, render_template, request
import json
import time

app = Flask(__name__)

with open('tasks.json') as json_file:
    todo = json.load(json_file)

def render():
    save()
    return render_template(
        'index.html',
        list=todo
    )

def save():
    with open('tasks.json', 'w') as outfile:
        json.dump(todo, outfile)

@app.route('/')
def home():
    return render()

@app.route('/add')
def add():
 	return render_template('submit.html')

@app.route('/delete/<task_time>')
def delete(task_time):
    for i in todo:
        if (todo[i]['time'] == int(task_time)):
            todo[i]['done'] = True

    return render()

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = list(request.form.items())
        title = result[0][1]
        desc = result[1][1]

        todo[title] = {
            'time': int(time.time()),
            'done': False,
            'desc': desc
        }

        return render()

if __name__ == '__main__':
    app.run(debug=True)

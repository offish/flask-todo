from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

with open('tasks.json') as json_file:
    todo = json.load(json_file)

def render():
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

@app.route('/delete/<task_id>')
def delete(task_id):
    for i in todo:
        if (todo[i]['id'] == int(task_id)):
            todo[i]['done'] = True

    save()
    return render()

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        task = []

        for key, value in result.items():
            task.append(value)

        todo[task[0]] = {
            'id': len(todo),
            'done': False,
            'desc': task[1]
        }

        save()
        return render()

if __name__ == '__main__':
    app.run(debug=True)

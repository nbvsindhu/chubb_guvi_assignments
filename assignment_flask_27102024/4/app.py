from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'POST':
        task = request.form['task']
        if task: 
            tasks.append(task)

    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)

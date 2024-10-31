from flask import Flask, render_template, request, redirect

app = Flask(__name__)

list = []

@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        feedback = request.form['feedback']
        list.append({'name': name, 'feedback': feedback})
        return redirect('/')  
    return render_template('index.html', feedbacks=list)

if __name__ == '__main__':
    app.run(debug=True)

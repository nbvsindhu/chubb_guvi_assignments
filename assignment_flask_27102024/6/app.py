from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == "user" and password == "password":
            message = "Welcome, user!"
        else:
            message = "Invalid credentials, please try again."

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

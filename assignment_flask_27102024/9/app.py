from flask import Flask, render_template

app = Flask(__name__)

users = [
    {"name": "abc", "age": 20, "city": "Hyd"},
    {"name": "pqr", "age": 19, "city": "Mumbai"},
    {"name": "xyz", "age": 21, "city": "Chennai"},
]

@app.route('/')
def user_table():
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 
def index():
    return ('<a href="/bio"> Link for bio </a>')

@app.route('/bio')
def bio():
    personal_info = {
        "name": "Sindhu",
        "age": 21,  
        "hobby": "dancing"  
    }
    return render_template('bio.html', info=personal_info)

if __name__ == '__main__':
    app.run(debug=True)

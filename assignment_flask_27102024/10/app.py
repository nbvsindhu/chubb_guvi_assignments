from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def temperature_converter():
    f = None
    if request.method == 'POST':
        c = float(request.form['c'])
        f = (c * 9/5) + 32
    
    return render_template('index.html', f=f)

if __name__ == '__main__':
    app.run(debug=True)

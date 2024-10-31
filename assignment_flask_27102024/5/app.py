from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    	"Honesty is best Policy",
	"Practice makes a man perfect",
	"You must be the change you wish to see in the world",
	"The way to get started is to quit talking and begin doing",
	"The future belongs to those who believe in the beauty of their dreams"
]

@app.route('/')
def quote():
    random_quote = random.choice(quotes)
    return render_template('index.html', quote=random_quote)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template,  request
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def home():
    #  this servers the html form
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def calculate_age():

    try:
        birth_year = int(request.form['birth_year'])
        current_year = datetime.now().year

        if birth_year > current_year or birth_year < 1900:

            return render_template('index.html', error="Please enter a valid birth year.")

        age = current_year - birth_year

        return render_template('index.html', age=age)

    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter a numeric birth year.")


if __name__ == '__main__':
    app.run(debug=True)

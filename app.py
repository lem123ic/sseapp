from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def details():
    return render_template('details.html')

@app.route('/existing_user', methods=['POST'])
def existing_user():
    name = request.form['name']
    user_data = get_user_by_name(name)

    if user_data:
        return render_template('existing_user.html', user=user_data)
    else:
        return render_template('existing_user.html', not_found=True)

@app.route('/submit_details', methods=['POST'])
def submit_details():
    name = request.form['name']
    age = request.form['age']


    save_user(name, age)  # Save user to the database

    return render_template('thank_you.html', name=name)

def save_user(name, age):
    # Connect to the database and save the user details
    with sqlite3.connect('user_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (name, age)
            VALUES (?, ?)
        ''', (name, age))
        conn.commit()

def get_user_by_name(name):
    # Retrieve user details from the database by name
    with sqlite3.connect('user_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
        user_data = cursor.fetchone()
        return user_data

if __name__ == '__main__':
    app.run(debug=True)


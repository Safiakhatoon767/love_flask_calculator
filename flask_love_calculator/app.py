from flask import Flask, render_template, request, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def calculate_love_percentage(name1, name2):
    combined_names = (name1 + name2).lower()
    unique_chars = set(combined_names)
    score = sum(ord(char) for char in unique_chars) % 101
    return score

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    name1 = request.form.get('name1')
    name2 = request.form.get('name2')
    if not name1 or not name2:
        flash("Both names are required!", "error")
        return redirect(url_for('index'))
    love_percentage = calculate_love_percentage(name1, name2)
    message = generate_message(love_percentage)
    return render_template('result.html', name1=name1, name2=name2, percentage=love_percentage, message=message)

def generate_message(percentage):
    if percentage > 80:
        return "A match made in heaven! 🌟"
    elif 50 <= percentage <= 80:
        return "Things look promising! 💖"
    else:
        return "It's complicated, but love is always worth it! ❤️"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)
count_file = 'counter.txt'

def read_count():
    """Reads the current count from the file, returns 0 if the file doesn't exist."""
    if not os.path.exists(count_file):
        return 0
    with open(count_file, 'r') as file:
        return int(file.read().strip())

def write_count(count):
    """Writes the new count to the file."""
    with open(count_file, 'w') as file:
        file.write(str(count))

def increment_count():
    """Increments the count and saves it to the file."""
    current_count = read_count()
    new_count = current_count + 1
    write_count(new_count)
    return new_count

def reset_count():
    """Resets the count to 0 and saves it to the file."""
    write_count(0)
    return 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def increment():
    new_count = increment_count()
    return jsonify({'count': new_count})

@app.route('/reset', methods=['POST'])
def reset():
    new_count = reset_count()
    return jsonify({'count': new_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

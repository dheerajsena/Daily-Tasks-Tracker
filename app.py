from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)

# In-memory store for simplicity
tasks = []

# Modernized HTML Template
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <title>Task Tracker - Stand-Up Notes</title>
    <style>
        body { font-family: 'Arial', sans-serif; margin: 50px auto; max-width: 600px; background: #f8f9fa; color: #333; }
        h2 { color: #007BFF; }
        input[type=text] { width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box; }
        button { padding: 10px; background: #007BFF; color: white; border: none; cursor: pointer; }
        button:hover { background: #0056b3; }
        ul { list-style-type: none; padding: 0; }
        li { background: #fff; margin: 5px 0; padding: 10px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        textarea { width: 100%; padding: 10px; box-sizing: border-box; margin-top: 20px; border-radius: 4px; }
    </style>
</head>
<body>
    <h2>Daily Task Tracker</h2>
    <form method="post">
        <input type="text" name="task" placeholder="Enter task completed..."><br>
        <button type="submit">Add Task</button>
    </form>

    <h2>Today's Tasks</h2>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>

    <h2>Stand-Up Meeting Notes - {{ date }}</h2>
    <textarea rows="8">{{ notes }}</textarea>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task'].strip()
        if task:
            tasks.append(task)

    date_today = datetime.now().strftime("%Y-%m-%d")
    notes = '\n'.join(f"- {task}" for task in tasks)

    return render_template_string(HTML_TEMPLATE, tasks=tasks, notes=notes, date=date_today)

@app.route('/clear', methods=['GET'])
def clear_tasks():
    tasks.clear()
    return jsonify({"status": "cleared"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

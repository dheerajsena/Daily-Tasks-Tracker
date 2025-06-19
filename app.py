from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)

# In-memory store for simplicity; use a database for persistent storage
tasks = []

# HTML Template for simplicity
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <title>Daily Task Tracker</title>
</head>
<body>
    <h2>Enter Task</h2>
    <form method="post">
        Task Description: <input type="text" name="task"><br>
        <button type="submit">Add Task</button>
    </form>
    <h2>Today's Tasks</h2>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
    <h2>Stand-Up Meeting Notes ({{ date }})</h2>
    <textarea rows="10" cols="50">{{ notes }}</textarea>
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
    app.run(debug=True)

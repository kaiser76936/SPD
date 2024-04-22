import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    TOP_DIR='~/SPD2/SPD/2'
    python_projects = []
    for directory in os.listdir(TOP_DIR):
        index_path = os.path.join(TOP_DIR, directory, 'htmlcov/index.html')
        if os.path.exists(index_path):
            python_projects.append(directory)

    return render_template('index.html', files=python_projects)
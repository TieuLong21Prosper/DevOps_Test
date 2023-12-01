from flask import Flask, jsonify, request

app = Flask(__name__)

# A simple list to store tasks
tasks = [
    {'id': 1, 'title': 'Learn Python', 'done': False},
    {'id': 2, 'title': 'Build a Flask App', 'done': False}
]

# Define a route for the endpoint '/tasks'
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Define a route for the endpoint '/tasks/<int:task_id>'
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    return jsonify({'task': task}) if task else jsonify({'message': 'Task not found'}), 404

# Define a route for the endpoint '/tasks', method POST
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'message': 'Invalid request, title is required'}), 400

    new_task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'done': False
    }

    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

if __name__ == '__main__':
    # Use environment variables to set host and port dynamically
    host = '0.0.0.0'
    port = 5000  # You can change this port if needed

    # Run the app using Gunicorn
    from gunicorn import util
    util.check_version("18.0.0")
    from gunicorn.app.wsgiapp import WSGIApplication
    WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]").run()

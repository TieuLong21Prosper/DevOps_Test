from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {'id': 1, 'title': 'Modified Learn Jenkins', 'done': False},
    {'id': 2, 'title': 'Build a Flask App', 'done': False}
]

# Define a route for the endpoint '/tasks'
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Define a route for the endpoint '/tasks', method GET
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
    app.run(debug=True, host='0.0.0.0', port=5000)


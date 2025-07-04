## Rest APIs in Flask
## Put and Delete operations in Flask
## Working with API'S json

from flask import Flask, jsonify, request

app = Flask(__name__)

## Inital Data in my to do list
todos = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Bread, Eggs',
        'done': False
    },
    {
        'id': 2,
        'title': 'Walk the dog',
        'description': 'Take the dog for a walk in the park',
        'done': False
    }
]


@app.route('/todos', methods=['GET'])
def get_todos():
    """
    Get all todos
    """
    return jsonify(todos)

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """
    Get a specific todo by ID
    """
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo: ### or If item is not None
        return jsonify(todo)
    else:
        return jsonify({'error': 'Todo not found'}), 404
    
@app.route('/todos', methods=['POST'])
def create_todo():
    if not request.json or not 'title' in request.json:
        return jsonify({'error': 'Bad request'}), 400
    new_item={
        "id": todos[-1]["id"] + 1 if todos else 1,
        "title": request.json['title'],
        "description": request.json.get('description', ''),
        "done": request.json.get('done', False)
    }
    todos.append(new_item)
    return jsonify(new_item), 201


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    todo['title'] = request.json.get('title', todo['title'])
    todo['description'] = request.json.get('description', todo['description'])
    todo['done'] = request.json.get('done', todo['done'])
    return jsonify(todo)

if __name__ == '__main__':
    app.run(debug=True)
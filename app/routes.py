from flask import Blueprint, request, redirect, url_for, current_app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = current_app.db.users.find()
    user_list = ''.join([
        f"<li>{user['name']} ({user['email']}) - <a href='/delete/{user['_id']}'>Delete</a></li>"
        for user in users
    ])
    return f'''
        <h1>Users</h1>
        <a href="/add">Add User</a>
        <ul>{user_list}</ul>
    '''

@main.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        current_app.db.users.insert_one({'name': name, 'email': email})
        return redirect(url_for('main.index'))

    return '''
        <h1>Add User</h1>
        <form method="POST">
            Name: <input type="text" name="name" required><br>
            Email: <input type="email" name="email" required><br>
            <input type="submit" value="Add">
        </form>
        <a href="/">Back</a>
    '''

@main.route('/delete/<user_id>')
def delete_user(user_id):
    from bson.objectid import ObjectId
    current_app.db.users.delete_one({'_id': ObjectId(user_id)})
    return redirect(url_for('main.index'))

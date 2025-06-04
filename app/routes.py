from flask import Blueprint, render_template, request, redirect, url_for, current_app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = current_app.db.users.find()
    return render_template('index.html', users=users)

@main.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        current_app.db.users.insert_one({'name': name, 'email': email})
        return redirect(url_for('main.index'))
    return render_template('add_user.html')

@main.route('/delete/<user_id>')
def delete_user(user_id):
    from bson.objectid import ObjectId
    current_app.db.users.delete_one({'_id': ObjectId(user_id)})
    return redirect(url_for('main.index'))

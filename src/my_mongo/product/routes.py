#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home_page():
    results = 'commented out mongo call'
    return render_template('indexjqy.html', results=results)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()


@app.route('/uploads/<path:filename>', methods=['POST'])
def save_upload(filename):
    mongo.save_file(filename, request.files['file'])
    return redirect(url_for('get_upload', filename=filename))


@app.route('/uploads/<path:filename>')
def get_upload(filename):
    return mongo.send_file(filename)


@app.route('/user/<username>')
def user_profile(username):
    user = mongo.db.users.find_one_or_404({'_id': username})
    return render_template('user.html', user=user)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == '__main__':
    app.run(host='0.0.0.0')

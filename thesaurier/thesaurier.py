from flask import Flask, request, render_template, url_for, redirect

DEBUG = True
SECRET_KEY = 'foobar'
USERNAME = 'admin'
PASSWORD = 'foobar'

app = Flask(__name__)
app.config.from_object(__name__)

if __name__ == '__main__':
    app.run()

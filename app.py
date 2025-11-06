from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.jinja2')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.jinja2')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.jinja2')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.jinja2')


if __name__ == '__main__':
    app.run()

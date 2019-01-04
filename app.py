from flask import *
from user import *
from blog import *
from forms import *
import functools

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)

@app.route('/init')
def init():
    init_users()
    init_blogs()
    return 'db initialised'

@app.route('/')
def index():
    form = LoginForm(request.form)
    if 'username' in session:
        posts = get_blogs()
        return render_template('index.html', posts = posts)
    else:
        return render_template('login.html', form = form)


@app.route('/login',  methods=('GET', 'POST'))
def login():
    login_form = LoginForm(request.form)
    error = None
    if request.method == 'POST':
        user = get_user(login_form.id.data, login_form.password.data)
        if user is None:
            error = 'Wrong username and password'
        else:
            session['username'] = user.username
            return redirect(url_for('index'))
        flash(error)
    return render_template('login.html', form=login_form)

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        username = form.id.data
        password = form.password.data
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            create_user(username, password)
            return redirect(url_for('login'))
        flash(error)
    return render_template('register.html', form=form)

@app.route('/update')
def update():
    return render_template('under_construction.html')

@app.route('/create')
def create():
    return render_template('under_construction.html')

@app.route('/logout', methods=('GET', 'POST'))
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=80)

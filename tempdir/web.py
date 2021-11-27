from flask import Flask, request, render_template, redirect, flash, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user

web = Flask(__name__)
web.secret_key = "supersecretkey"

web.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UserList.sqlite'
web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(web)


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id =  db.Column(db.Integer, primary_key=True)
    user_firstname = db.Column(db.String(50))
    user_lastname = db.Column(db.String(50))
    user_username = db.Column(db.String(50))
    user_password = db.Column(db.String(50))

    def __init__(self, user_firstname, user_lastname, user_username, user_password):
        self.user_firstname = user_firstname
        self.user_lastname = user_lastname
        self.user_username = user_username
        self.user_password = user_password

login_manager = LoginManager()
login_manager.init_app(web)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@web.before_first_request
def create_tables():
    db.create_all()

@web.route("/", methods=['GET', 'POST'])
def login():
    global username, password, user_name,  user_pass
    if request.method == "GET":
        return render_template("login.html")
        
    if request.method == "POST":
        user_username = request.form['username'] 
        user_password = request.form['password']

        user = User.query.filter_by(user_username=user_username, user_password=user_password).first()
        if user:
            session['name'] = user_username
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid Username or Password!')
            return redirect('/')
    return render_template("login.html")

@web.route("/register", methods=['GET', 'POST'])
def register():
    global user_firstname, user_lastname, user_username, user_password, password2
    if request.method == "GET":
        return render_template('register.html')
        
    if request.method == "POST":
        user_firstname = request.form['firstname'] 
        user_lastname = request.form['lastname']
        user_username = request.form['username']
        user_password = request.form['userpass']
        password2 = request.form['confirmpass']
        usercheck = User.query.filter_by(user_username=user_username).first()

        if usercheck:
            flash('Username Already Taken!')
            return redirect('/register')
        else:
            if password2 == user_password:
                new_user = User(user_firstname, user_lastname, user_username, user_password)
                db.session.add(new_user)
                db.session.commit()
                flash('Account Created!')
                return redirect('/')
            else: 
                flash('Password Not Match!')
                return redirect('/register')

    else: 
        return render_template('register.html')

@web.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@web.route("/home")
@login_required
def home():
    global username
    username = session.get('name', None)
    return render_template("index.html", username = username)

if __name__ == "__main__":
    web.run(host="0.0.0.0", port=8080,debug=True)

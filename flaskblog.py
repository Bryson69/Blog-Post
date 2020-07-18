from flask import Flask , render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


# "Import flask and render template ,
app = Flask(__name__)# app is a flask variable whihc is set to an instance ,Add flask variable,


app.config['SECRET_KEY'] = 'c7f3e00d51e9c47c506c8d05ec7d027d'

# 
#  Add dictionary which represents a single blog post"
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'Forst Post Content',
        'date_posted': 'June 16 , 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'June 1 , 2020'
    }
]


#  Add an app route for the home and about page ,
@app.route("/")
@app.route("/home")
def home():
    return render_template ('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template ('about.html', title = 'About')


@app.route("/game")
def game():
    return render_template ('game.html')


@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)


@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'passwprd':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unseccessful. Please check your username and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)


if __name__ == '__main__':
    app.run(debug = True)
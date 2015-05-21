from flask import Flask, render_template, flash, request, url_for, redirect, session
from dbconnect import connection
from forms import RegistrationForm

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template("main.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data, form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == "__main__":
	app.run()
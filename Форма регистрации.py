from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime
from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    email = StringField('Login / email', validators=[DataRequired()])
    password = PasswordField('Password')
    repeatPassword = PasswordField('Repeat password',
                                   validators=[DataRequired(),
                                               EqualTo('password')])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


def get_css():
    return url_for('static', filename='css/style.css')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init('db/martians.db')


def main():
    app.run()


@app.route('/')
def index():
    session = db_session.create_session()
    param = {
        'jobs': session.query(Jobs).all(),
        'css': get_css()
    }
    return render_template('works_log.html', **param)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    param = {
        'css': get_css(),
        'form': form,
        'title': 'Регистрация'
    }
    if form.validate_on_submit():
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', **param,
                                   message='Такой пользователь уже есть')
        user = User(surname=form.surname.data,
                    name=form.name.data,
                    age=form.age.data,
                    position=form.position.data,
                    speciality=form.speciality.data,
                    address=form.address.data,
                    email=form.email.data)

        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/')
    return render_template('register.html', **param)


if __name__ == '__main__':
    main()

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms.fields.html5 import EmailField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


def emailCheck(form, field):
    # if '@' not in field.data:
    #     raise ValidationError("Please include an '@' in an email address. \
    #     {input} is missing an '@'.".format(input=str(field.data)))
    if "utoronto" not in field.data:
        field.data = "Please use your UofT email."



class Form(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    # email = EmailField('What is your UofT Email address?', validators=[DataRequired(), emailCheck])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        # if old_email is not None and old_email != form.email.data:
        #     flash('Looks like you have changed your email!')
        session['name'] = form.name.data
        # session['email'] = form.email.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))
    # return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())


if __name__ == '__main__':
    app.run()

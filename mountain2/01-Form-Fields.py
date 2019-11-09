from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (TextField,TextAreaField,SubmitField)
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
class InfoForm(FlaskForm):
   
    answer1 = TextAreaField()
    answer2 = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():

    form = InfoForm()
    if form.validate_on_submit():
        session['answer1'] = form.answer1.data
        session['answer2'] = form.answer2.data
        return redirect(url_for("thankyou"))


    return render_template('components.html', form=form)


@app.route('/thankyou')
def thankyou():

    return render_template('01-thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)

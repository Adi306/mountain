from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (TextField,TextAreaField,SubmitField)
from wtforms.validators import DataRequired
app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html')
app.config['SECRET_KEY'] = 'mysecretkey'
class InfoForm(FlaskForm):

    answer1 = TextAreaField()
    answer2 = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/test',methods=['GET', 'POST'])

def test():

    form = InfoForm()
    if form.validate_on_submit():
        session['answer1']= form.answer1.data
        session['answer2']= form.answer2.data
        session['answer1'] += session['answer2']
        return redirect(url_for("thankyou"))


    return render_template('components.html', form=form)
@app.route('/thankyou')
def thankyou():

    return render_template('thankyou.html', prediction_text= "Your Personality type: {}".format(session['answer1']))
@app.route('/about')
def about():

    return render_template('project.html')


if __name__ == '__main__':
    app.run(debug=True)

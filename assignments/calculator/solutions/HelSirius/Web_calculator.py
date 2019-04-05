from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
import os


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY



class CalculateForm(FlaskForm):

    First_Num  = IntegerField('First Number')
    Second_Num = IntegerField('Second Number')
    plus = SubmitField('Addition')
    minus = SubmitField('Substraction')
    multiply = SubmitField('Multiplication')
    divide = SubmitField('Division')

@app.route('/',methods = ['GET','POST'])
def index():
	form =CalculateForm()

	if form.validate_on_submit():
		First_Num = request.form.get ('First_Num', type=int)
		Second_Num = request.form.get ('Second_Num', type=int)

		if form.plus.data:
			add = First_Num + Second_Num
		elif form.minus.data:
			substract = First_Num - Second_Num
		elif form.multiply.data:
			mult = First_Num * Second_Num
		elif form.divide.data:
			divide = First_Num / Second_Num
		return render_template('calculator.html',**locals())
	return render_template('calculator.html',form=form)
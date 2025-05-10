from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class Registrationform(FlaskForm):
    username=StringField("Username",validators=[DataRequired(),Length(min=2,max=20)])   #by datarequired it can't be empty and length will be used as given
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    confirm_password=PasswordField("Confirm password",validators=[DataRequired(),EqualTo("password")])     # to equate password and confirm password equalTo is used
    submit=SubmitField("Sign Up")


class Loginform(FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    remember_me=BooleanField("Remember Me")
    submit=SubmitField("Login")
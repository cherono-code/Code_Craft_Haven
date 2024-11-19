# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Email
from flask_wtf.recaptcha import RecaptchaField

class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[InputRequired()])
    email = EmailField('Your Email', validators=[InputRequired(), Email()])
    message = TextAreaField('Your Message', validators=[InputRequired()])
    recaptcha = RecaptchaField()  # Adds Google reCAPTCHA to the form

class RegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    phone = StringField('Phone Number', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    organization = StringField('Organization / Institution')
    role = RadioField('Role | Position', choices=[('developer', 'Developer'), 
                                                 ('designer', 'Designer'),
                                                 ('devops', 'DevOps'),
                                                 ('other', 'Other')], 
                      validators=[InputRequired()])
    other_role = StringField('Please specify your role', default='', validators=[InputRequired()])
    proficiency = RadioField('How would you rate your coding proficiency?', 
                             choices=[('beginner', 'Beginner'), 
                                      ('intermediate', 'Intermediate'),
                                      ('expert', 'Expert')],
                             validators=[InputRequired()])
    recaptcha = RecaptchaField()  # reCAPTCHA for form submission
# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Email
from flask_wtf.recaptcha import RecaptchaField

class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[InputRequired()])
    email = EmailField('Your Email', validators=[InputRequired(), Email()])
    message = TextAreaField('Your Message', validators=[InputRequired()])
    recaptcha = RecaptchaField()  # Adds Google reCAPTCHA to the form

class RegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    phone = StringField('Phone Number', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    organization = StringField('Organization / Institution')
    role = RadioField('Role | Position', choices=[('developer', 'Developer'), 
                                                 ('designer', 'Designer'),
                                                 ('devops', 'DevOps'),
                                                 ('other', 'Other')], 
                      validators=[InputRequired()])
    other_role = StringField('Please specify your role', default='', validators=[InputRequired()])
    proficiency = RadioField('How would you rate your coding proficiency?', 
                             choices=[('beginner', 'Beginner'), 
                                      ('intermediate', 'Intermediate'),
                                      ('expert', 'Expert')],
                             validators=[InputRequired()])
    recaptcha = RecaptchaField()  # reCAPTCHA for form submission

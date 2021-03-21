from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,DateField,BooleanField,SelectField,SubmitField
from wtforms.validators import DataRequired,EqualTo,Length,Email,email_validator,ValidationError


class PersonRegisterForm(FlaskForm):
    username = StringField("Username",render_kw={"placeholder": "Username"},
                        validators=[DataRequired(),Length(min=1,max=40)]) 
    fullname = StringField("Full Name",render_kw={"placeholder": "Full Name"},
                        validators=[DataRequired(),Length(min=1,max=40)]) 
    email = StringField('Email',render_kw = {"placeholder": "Email"},
                        validators = [DataRequired(),Email()])

    password = PasswordField('Password',validators = [DataRequired(),
                            Length(min=4)],render_kw={'placeholder':'Passowrd'})

    confirm_password = PasswordField('Password',validators=[DataRequired(),Length(min=4),EqualTo('password')],render_kw={'placeholder':'Confirm Passowrd'})
    birth_date = DateField("Date of Birth",validators=[DataRequired()],format='%Y-%m-%d')
    
    gender = SelectField(
        'Gender',
        choices = [('gender', 'Gender') ,('male', 'Male'), ('feamle', 'Feamle')],validators=[DataRequired()]
    )
    submit = SubmitField("Sign Up")

    def validate_gender(self, gender):
        if gender.data=='gender':
            raise ValidationError('Input value')
    